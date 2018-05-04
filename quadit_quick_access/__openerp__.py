# -*- coding: utf-8 -*-
# © <2016> <QuadIT>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "QuadIT - Quick Access",
    "summary": "Quick Access Menu",
    "author": "QuadIT",
    "website": "https://www.quadit.mx",
    "category": "Hidden",
    "version": "0.1",
    "depends": [
        "base",
        "account",
        "product",
        "hr",
        "sale",
        "stock",
    ],
    "application": True,
    "installable": True,
    "data": [
        "security/ir.model.access.csv",
        "views/menu.xml",
        "views/empresas_view.xml",
        "views/sucursales_view.xml",
        "views/departamentos_view.xml",
    ],
    "demo": [],
}
