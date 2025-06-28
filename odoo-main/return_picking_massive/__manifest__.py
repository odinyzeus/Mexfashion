# -*- coding: utf-8 -*-
# Copyright 2024 CEIVRYA SAS de CV
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    'name': "Return Multiple Packing Massive",
    'description': """
            Return Packing Multiple Operation Confirm by Action Menu
    """,
    'author': 'PhD. Eduardo Vargas',
    'license': 'LGPL-3',
    'website': 'https://ceivrya.com',
    'category': 'sales',
    'version': '17.0.0.0.11',
    'depends': ['stock',   # Dependencia necesaria para personalizar la vista Kanban de Picking
    ],
    'data': [
        'views/stock_picking.xml',    # Archivo que crea la funcionalidad de devoluciones masivas'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,    
}