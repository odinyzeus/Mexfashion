from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    product_id = fields.Many2one('product.product', string='Producto Global CFDI')
    tax_id = fields.Many2one('account.tax', string='Impuesto a aplicar')
    cfdi_usage = fields.Selection(selection=[('S01', 'Sin efectos fiscales'), ('G03', 'Gastos en general')], string='Uso CFDI por defecto')
    payment_method_id = fields.Many2one('l10n_mx_edi.payment.method', string='Método de pago por defecto')
    payment_form = fields.Selection(selection=[('01', 'Efectivo'), ('03', 'Transferencia electrónica')], string='Forma de pago por defecto')
    allow_different_currencies = fields.Boolean(string='Permitir diferentes monedas')
    allow_missing_rfc = fields.Boolean(string='Permitir clientes sin RFC')

    def get_values_cfdi_config(self):
        return {
            'product_id': int(self.env['ir.config_parameter'].sudo().get_param('global_cfdi_invoice.product_id', default=0)),
            'tax_id': int(self.env['ir.config_parameter'].sudo().get_param('global_cfdi_invoice.tax_id', default=0)),
            'cfdi_usage': self.env['ir.config_parameter'].sudo().get_param('global_cfdi_invoice.cfdi_usage', default='S01'),
            'payment_method_id': int(self.env['ir.config_parameter'].sudo().get_param('global_cfdi_invoice.payment_method_id', default=0)),
            'payment_form': self.env['ir.config_parameter'].sudo().get_param('global_cfdi_invoice.payment_form', default='01'),
            'allow_different_currencies': self.env['ir.config_parameter'].sudo().get_param('global_cfdi_invoice.allow_different_currencies', default='False') == 'True',
            'allow_missing_rfc': self.env['ir.config_parameter'].sudo().get_param('global_cfdi_invoice.allow_missing_rfc', default='False') == 'True',
        }

    def set_values(self):
        super().set_values()
        self.env['ir.config_parameter'].sudo().set_param('global_cfdi_invoice.product_id', self.product_id.id)
        self.env['ir.config_parameter'].sudo().set_param('global_cfdi_invoice.tax_id', self.tax_id.id)
        self.env['ir.config_parameter'].sudo().set_param('global_cfdi_invoice.cfdi_usage', self.cfdi_usage)
        self.env['ir.config_parameter'].sudo().set_param('global_cfdi_invoice.payment_method_id', self.payment_method_id.id)
        self.env['ir.config_parameter'].sudo().set_param('global_cfdi_invoice.payment_form', self.payment_form)
        self.env['ir.config_parameter'].sudo().set_param('global_cfdi_invoice.allow_different_currencies', str(self.allow_different_currencies))
        self.env['ir.config_parameter'].sudo().set_param('global_cfdi_invoice.allow_missing_rfc', str(self.allow_missing_rfc))
