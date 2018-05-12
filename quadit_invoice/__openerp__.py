# -*- coding: utf-8 -*-
# © <2017> <Quadit, S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{

    'name': 'Custom Invoice Report',
    'summary': 'Inherit Invoice Report',
    'version': '8.0.1.0.0',
    'category': 'Account & Finance',
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
        'account',
    ],
    'data': [
        'views/report_invoice.xml'
    ],
}
