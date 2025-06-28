# -*- coding: utf-8 -*-

from odoo import models, fields

class StockMove(models.Model):
    _inherit = 'stock.move.line'

    origin_document = fields.Char(
        string='Documento Original',
        related='origin',
        store=True,
        readonly=True
    )
