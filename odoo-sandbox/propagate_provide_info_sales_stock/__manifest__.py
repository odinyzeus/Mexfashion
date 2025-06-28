# -*- coding: utf-8 -*-
# Copyright 2024 CEIVRYA SAS de CV
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    'name': "Propagate Provide Info Sales Stock",
    'description': """
            Propagate Provide Info Sales to Barcode Stock.
    """,
    'author': 'PhD. Eduardo Vargas B.',
    'license': 'LGPL-3',
    'website': 'https://www.ceivrya.com',
    'category': 'Stock',
    'version': '17.0.1.0.2',
    'depends': ['sale_stock', 'stock', 'stock_barcode'],
    'data': [
        'views/views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'propagate_provide_info_sales_stock/static/src/**/*.js',
            'propagate_provide_info_sales_stock/static/src/**/*.xml',
        ],
    }   
}

