# -*- coding: utf-8 -*-

from odoo import models, _
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def confirm_sale_orders(self):
        """
        Server action to confirm multiple selected sales orders.
        """
        if not self:
            raise UserError(_('You must select at least one sales order to confirm.'))
        
        if self.filtered(lambda order: order.state != 'draft'):
            raise UserError(_('Only draft orders can be confirmed.'))
            
        # Filter only orders in draft state
        draft_orders = self.filtered(lambda order: order.state == 'draft')
        
        if not draft_orders:
            raise UserError(_('There are no draft orders to confirm.'))
        
        # Counter for logging
        confirmed_count = 0
        error_orders = []
        
        for order in draft_orders:
            try:  
                order.action_confirm()
                confirmed_count += 1
                    
                order.message_post(
                    body=_("Order automatically confirmed via mass action."),
                    message_type='notification'
                )
                    
            except Exception as e:
                error_orders.append(f"{order.name} ({_('Error')}: {str(e)})")
                continue
        
        # Prepare result message
        message = _("{} sales orders have been confirmed.").format(confirmed_count)
        if error_orders:
            message += _("\n\nThe following orders could not be confirmed:\n")
            message += "\n".join(error_orders)
        
        # Show notification to the user
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Sales Order Confirmation'),
                'message': message,
                'type': 'info' if confirmed_count > 0 else 'warning',
                'sticky': True,
                'next': {'type': 'ir.actions.act_window_close' }
            }
        }
