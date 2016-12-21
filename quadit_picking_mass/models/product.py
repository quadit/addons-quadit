# -*- coding: utf-8 -*-
# © <2016> <Quad IT>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class ProductProduct(models.Model):

    _inherit = 'product.product'

    default = fields.Boolean(string='Default')
