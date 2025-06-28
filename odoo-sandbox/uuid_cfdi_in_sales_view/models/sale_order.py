# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    folios_fiscales = fields.Char(
        string='Folios fiscales',
        compute='_compute_folios_fiscales',
        help='Listado de folios fiscales relacionados con la orden de venta'
    )

    @api.depends('invoice_ids.l10n_mx_edi_cfdi_uuid')
    def _compute_folios_fiscales(self):
        for order in self:
            # obtenemos sólo facturas de venta (out_invoice)
            folios = order.invoice_ids \
                .filtered(lambda m: m.move_type == 'out_invoice') \
                .mapped('l10n_mx_edi_cfdi_uuid')
            order.folios_fiscales = ', '.join(f for f in folios if f)
