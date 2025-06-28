{
    "name": "Factura Global CFDI 4.0 v4",
    'description': """
            This module produce global invoice
    """,
    'version': '17.0.0.1',
    "author": "PhD Eduardo Vargas Bernardino",
    'website': 'https://ceivrya.com',
    "category": "Accounting",
    "depends": ["base", "sale", "account", "l10n_mx_edi"],
    "data": [
        "views/sale_advance_payment_inv_view.xml",
#        "views/account_move_view.xml",
#        "views/res_config_settings_view.xml"
    ],
    'installable': True,
    'application': False,
    "post_init_hook": "post_init_hook",
    "auto_install": False
}
