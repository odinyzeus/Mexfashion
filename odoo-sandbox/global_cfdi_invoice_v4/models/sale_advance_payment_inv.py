from odoo import models, fields, _
from odoo.exceptions import UserError
from itertools import groupby
from operator import attrgetter

class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = 'sale.advance.payment.inv'

    use_cfdi_global = fields.Boolean(string="Factura Global CFDI 4.0")

    def create_invoices(self):
        if self.use_cfdi_global:
            config = self.env['res.config.settings'].get_values_cfdi_config()

            all_orders = self.env['sale.order'].browse(self._context.get('active_ids', []))
            if not all_orders:
                return

            if not config['allow_different_currencies']:
                currencies = all_orders.mapped('currency_id')
                if len(currencies) > 1:
                    raise UserError(_("No se puede generar una factura global con órdenes en diferentes monedas."))

            product = self.env['product.product'].browse(config['product_id'])
            if not product:
                raise UserError(_("No se encontró el producto configurado para facturación global."))

            invoices = self.env['account.move']
            for partner, orders in groupby(all_orders.sorted(key=lambda o: o.partner_id.id), key=attrgetter('partner_id')):
                orders = self.env['sale.order'].browse([o.id for o in orders])

                if not config['allow_missing_rfc'] and not partner.vat:
                    raise UserError(_("El cliente %s no tiene un RFC válido.") % partner.name)

                invoice_vals = {
                    'move_type': 'out_invoice',
                    'partner_id': partner.id,
                    'currency_id': orders[0].currency_id.id,
                    'invoice_origin': 'Ordenes: ' + ', '.join(orders.mapped('name')),
                    'invoice_line_ids': [],
                    'global_sale_order_ids': [(6, 0, orders.ids)],
                    'l10n_mx_edi_usage': partner.l10n_mx_edi_usage or config['cfdi_usage'],
                    'l10n_mx_edi_payment_method_id': partner.l10n_mx_edi_payment_method_id.id if partner.l10n_mx_edi_payment_method_id else config['payment_method_id'],
                    'l10n_mx_edi_payment_form': partner.l10n_mx_edi_payment_form or config['payment_form'],
                }

                for order in orders:
                    line = {
                        'product_id': product.id,
                        'name': f"Orden {order.name}",
                        'quantity': 1,
                        'price_unit': order.amount_untaxed,
                        'tax_ids': [(6, 0, config['tax_id'])],
                    }
                    invoice_vals['invoice_line_ids'].append((0, 0, line))

                invoice = self.env['account.move'].create(invoice_vals)
                invoice.action_post()
                invoices += invoice

            action = self.env.ref('account.action_move_out_invoice_type')
            result = action.read()[0]
            if len(invoices) == 1:
                result.update({
                    'views': [(self.env.ref('account.view_move_form').id, 'form')],
                    'res_id': invoices.id,
                })
            else:
                result.update({
                    'domain': [('id', 'in', invoices.ids)],
                })
            return result

        return super().create_invoices()
