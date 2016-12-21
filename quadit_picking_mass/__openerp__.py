# -*- coding: utf-8 -*-
# © <2016> <Quad IT>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Quad IT - Picking Massive",
    "summary": "This module create a form with which create a massive picking",
    "version": "8.0.1.0.0",
    "category": "Stock",
    "website": "http://www.quadit.com.mx/",
    "author": "<Quad IT>, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "base",
        "product",
        "stock",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/stock_view.xml",
        "views/product_view.xml",
    ],
    "demo": [],
    "qweb": [],
}
