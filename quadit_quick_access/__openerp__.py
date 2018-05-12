# -*- coding: utf-8 -*-
# © <2017> <Quadit, S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{

    'name': 'Quick Access',
    'summary': 'Quick Access Menu',
    'author': 'Quadit, S.A. de C.V., Odoo Community Association (OCA)',
    'website': 'https://www.quadit.mx',
    'category': 'Hidden',
    'version': '8.0.1.0.0',
    'license': 'AGPL-3',
    'depends': [
        'base',
        'account',
        'product',
        'hr',
        'sale',
        'stock',
    ],
    'application': False,
    'installable': True,
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/empresas_view.xml',
        'views/sucursales_view.xml',
        'views/departamentos_view.xml',
    ],
    'demo': [],
}
