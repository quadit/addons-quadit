# -*- coding: utf-8 -*-
# © <2016> <QuadIT>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class ResSucursales(models.Model):

    _name = 'res.sucursales'
    _description = 'Sucursales'

    empresa_id = fields.Many2one(
        comodel_name='res.empresas',
        string='Empresa')
    name = fields.Char(
        string='Sucursal')
    address = fields.Char(
        string='Dirección')
    phone = fields.Char(string='Teléfono')
    image = fields.Binary(
        string='Logo')
    active = fields.Boolean()
