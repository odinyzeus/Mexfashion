# -*- coding: utf-8 -*-

from odoo import models, _
from odoo.exceptions import UserError

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def ReturnPicking(self):
        StockReturnPicking = self.env['stock.return.picking']

        for picking in self:
            if picking.state != 'done':
                continue

            return_wizard = StockReturnPicking.with_context(
                active_id=picking.id,
                active_ids=[picking.id],
                active_model='stock.picking'
            ).create({
                'picking_id': picking.id,
            })

            return_lines = []
            for move in picking.move_ids_without_package.filtered(lambda m: not m.scrapped):
                qty_done = sum(move.move_line_ids.mapped('qty_done'))
                if qty_done > 0:
                    return_lines.append((0, 0, {
                        'product_id': move.product_id.id,
                        'quantity': qty_done,
                        'move_id': move.id,
                    }))

            return_wizard.product_return_moves = return_lines

            # Crear devolución
            return_data = return_wizard.create_returns()
            return_picking = self.env['stock.picking'].browse(return_data.get('res_id'))

            # 🛠 Forzar demanda correcta en movimientos de devolución
            for move in return_picking.move_ids_without_package:
                origin_move = move.origin_returned_move_id
                if origin_move:
                    qty_done = sum(origin_move.move_line_ids.mapped('qty_done'))
                    move.write({
                        'product_uom_qty': qty_done
                    })

        # return {'type': 'ir.actions.act_window',
        #         'res_model': 'stock.picking',
        #         'res_id': return_picking.id,
        #         'view_mode': 'form',
        #         'target': 'current',
        #         }



        #     return_picking.action_assign()
        #     for move_line in return_picking.move_line_ids:
        #         move_line.qty_done = move_line.product_uom_qty
        #     return_picking.button_validate()
