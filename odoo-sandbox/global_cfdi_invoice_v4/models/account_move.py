from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    global_sale_order_ids = fields.Many2many('sale.order', string='Órdenes asociadas')

    def action_view_sale_orders_cfdi(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Órdenes de Venta',
            'view_mode': 'tree,form',
            'res_model': 'sale.order',
            'domain': [('id', 'in', self.global_sale_order_ids.ids)],
        }
