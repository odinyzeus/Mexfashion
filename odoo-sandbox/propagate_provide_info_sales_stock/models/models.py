# -*- coding: utf-8 -*-

from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    shipping_guide = fields.Char(copy=False)
    purchase_order_name = fields.Char(copy=False)
    
class ProcurementGroup(models.Model):
    _inherit = 'procurement.group'

    shipping_guide = fields.Char(copy=False)
    purchase_order_name = fields.Char(copy=False)

    
class StockPicking(models.Model):
    _inherit = 'stock.picking'
    
    shipping_guide = fields.Char(copy=False)
    purchase_order_name = fields.Char(copy=False)
    
    def _get_fields_stock_barcode(self):
        # """ List of fields on the stock.picking object that are needed by the
        # client action. The purpose of this function is to be overridden in order
        # to inject new fields to the client action.
        # """
        res = super(StockPicking, self)._get_fields_stock_barcode()
        if res:
            res += ['shipping_guide']
            res += ['purchase_order_name']
        return res


class StockMove(models.Model):
    _inherit = 'stock.move'

    shipping_guide = fields.Char(related='picking_id.shipping_guide')
    purchase_order_name = fields.Char(related='picking_id.purchase_order_name')
    
    def _get_fields_stock_barcode(self):
        # """ List of fields on the stock.picking object that are needed by the
        # client action. The purpose of this function is to be overridden in order
        # to inject new fields to the client action.
        # """
        res = super(StockMove, self)._get_fields_stock_barcode()
        if res:
            res += ['shipping_guide']
            res += ['purchase_order_name']
        return res
    
    def _get_new_picking_values(self):
        res = super(StockMove, self)._get_new_picking_values()
        res['shipping_guide'] = self.group_id.sale_id.shipping_guide
        res['purchase_order_name'] = self.group_id.sale_id.purchase_order_name
        return res

    def _prepare_procurement_values(self):
        res = super(StockMove, self)._prepare_procurement_values()
        res['shipping_guide'] = self.group_id.sale_id.shipping_guide
        res['purchase_order_name'] = self.group_id.sale_id.purchase_order_name
        return res
