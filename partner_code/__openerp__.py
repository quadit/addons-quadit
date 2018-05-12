# -*- coding: utf-8 -*-
# © <2017> <Quadit, S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{

    'name': 'Partner Code',
    'summary': 'Add field code after name',
    'version': '8.0.1.0.0',
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
    ],
    'data': [
        'views/partner_view.xml',
    ],
}
