# -*- coding: utf-8 -*-
# © <2015> <Quad IT S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Sale Order Custom Report",
    "version": "8.0.1.0.0",
    "category": "Report",
    "website": "http://www.quadit.com.mx",
    "author": "<Quad IT S.A. de C.V.>, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "description": "Sale Order Report Custom",
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "sale",
    ],
    "data": [
        'reports/custom_sale_order.xml',
    ],
    "demo": [
    ],
    "qweb": [
    ]
}
