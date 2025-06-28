# -*- coding: utf-8 -*-
# Copyright 2024 CEIVRYA SAS de CV
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    'name': "Insert CFDI_UUID_values into Sales View",
    'description': """
            Insert a list of CFDI_UUID into sales View (Folios Fiscales).
    """,
    'author': 'PhD. Eduardo Vargas',
    'license': 'LGPL-3',
    'website': 'https://ceivrya.com',
    'category': 'sales',
    'version': '17.0.0.0.1',
    'depends': ['base','sale', 'account', 'l10n_mx_edi'],
    'data': [
        'views/cfdi_uuid_view.xml',    # File that contains the structure of personalized view'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,    
}
