# -*- coding: utf-8 -*-
# © <2017> <Quadit, S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class ProductProduct(models.Model):

    _inherit = 'product.product'

    default = fields.Boolean(string='Available in Production')
    default_sale = fields.Boolean(string='Available in Sales')
