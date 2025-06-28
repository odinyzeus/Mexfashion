
# -*- coding: utf-8 -*-
def post_init_hook(env):
    from odoo.api import Environment
    # si necesitas el cursor o el registry:
    cr = env.cr
    registry = env.registry
    env = Environment(cr, SUPERUSER_ID, {})

    # Buscar producto por código interno
    product = env['product.product'].search([('default_code', '=', 'GlobalCFDI')], limit=1)
    tax = env['account.tax'].search([('amount', '=', 16), ('type_tax_use', '=', 'sale')], limit=1)
    method = env['l10n_mx_edi.payment.method'].search([('code', '=', 'PUE')], limit=1)

    env['ir.config_parameter'].sudo().set_param('global_cfdi_invoice.product_id', product.id)
    env['ir.config_parameter'].sudo().set_param('global_cfdi_invoice.tax_id', tax.id)
    env['ir.config_parameter'].sudo().set_param('global_cfdi_invoice.cfdi_usage', 'S01')
    env['ir.config_parameter'].sudo().set_param('global_cfdi_invoice.payment_method_id', method.id)
    env['ir.config_parameter'].sudo().set_param('global_cfdi_invoice.payment_form', '01')
    env['ir.config_parameter'].sudo().set_param('global_cfdi_invoice.allow_different_currencies', 'False')
    env['ir.config_parameter'].sudo().set_param('global_cfdi_invoice.allow_missing_rfc', 'False')
