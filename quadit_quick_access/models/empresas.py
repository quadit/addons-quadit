# -*- coding: utf-8 -*-
# © <2016> <QuadIT>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class ResEmpresas(models.Model):

    _name = 'res.empresas'
    _description = 'Empresas'

    name = fields.Char(
        string='Empresas')
    image = fields.Binary(
        string='Logo')
    rfc = fields.Char(
        string='RFC')
    address = fields.Char(
        string='Dirección')
    zip = fields.Char(
        string='Código Postal')
    phone = fields.Char(
        string='Teléfono')
    mail = fields.Char(
        string='Correo Electrónico')