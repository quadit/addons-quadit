# -*- coding: utf-8 -*-
# © <2017> <Quadit, S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    line_default = fields.Boolean(string='Llenadas')

    @api.one
    def compute_lines(self):
        for rec in self:
            product_array = []
            product_obj = self.env['product.product']
            product_ids = product_obj.search([
                ('default_sale', '=', True),
            ])
            for product in product_ids:
                xline = (0, 0, {
                    "product_id": product.id,
                })
                product_array.append(xline)
            rec.order_line = [x for x in product_array]
            rec.line_default = True
