# -*- coding: utf-8 -*-
# © <2016> <QuadIT>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class ResDepartamentos(models.Model):

    _name = 'res.departamentos'
    _description = 'Departamentos'

    unidad = fields.Char(
        string='Unidad')
    codigo = fields.Char(string='Código')
    name = fields.Char(
        string='Nombre')
    image = fields.Binary(
        string='Logo')
