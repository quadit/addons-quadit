# -*- coding: utf-8 -*-
# © <2017> <Quadit, S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Hotel Reservation Send Mail',
    'summary': 'This module send mail when create or update hotel reservation',
    'author': 'Quadit, S.A. de C.V., Odoo Community Association (OCA)',
    'website': 'https://www.quadit.mx',
    'category': 'Hotel',
    'version': '8.0.1.0.0',
    'license': 'AGPL-3',
    'depends': [
        'base',
        'email_template',
        'hotel_reservation',
    ],
    'application': False,
    'installable': True,
    'data': [
        'views/email_template_view.xml',
    ],
}
