# -*- coding: utf-8 -*-
# Copyright 2024 CEIVRYA SAS de CV
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    'name': "Origin Source into Product Moves",
    'description': """
            Insert Origin Source into Product Moves
    """,
    'author': 'PhD. Eduardo Vargas',
    'license': 'LGPL-3',
    'website': 'https://ceivrya.com',
    'category': 'sales',
    'version': '17.0.0.0.1',
    'depends': ['stock',   # Dependencia necesaria para personalizar la vista Kanban de Picking
    ],
    'data': [
        'views/stock_move_view.xml',    # Archivo que crea la funcionalidad de devoluciones masivas'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,    
}
