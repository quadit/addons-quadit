# -*- coding: utf-8 -*-
# © <2016> <QuadIT>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "QuadIT - Report Invoice",
    "summary": "Inherit Report Invoice",
    "version": "8.0.1.0.0",
    "category": "Hidden",
    "website": "https://odoo-community.org/",
    "author": "<QuadIT>, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "base",
        "account",
    ],
    "data": [
        "views/report_invoice.xml"
    ],
    "demo": [],
    "qweb": []
}
