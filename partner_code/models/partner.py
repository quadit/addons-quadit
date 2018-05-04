# -*- coding: utf-8 -*-
# © <2017> <Quadit, S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class ResPartner(models.Model):

    _name = 'res.partner'
    _inherit = 'res.partner'

    partner_code = fields.Char(string='Code')
