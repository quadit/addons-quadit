# -*- coding: utf-8 -*-
# © <2017> <Quadit, S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{

    'name': 'Fake Picking Massive',
    'summary': 'This module create a form with which create a massive picking',
    'version': '8.0.0.1',
    'category': 'Stock',
    'website': 'https://www.quadit.mx',
    'author': 'Quadit, S.A. de C.V.',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'external_dependencies': {
        'python': [],
        'bin': [],
    },
    'depends': [
        'base',
        'product',
        'stock',
        'sale',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/stock_view.xml',
        'views/stock_picking_view.xml',
        'views/product_view.xml',
        'views/sale_view.xml',
    ],
}
