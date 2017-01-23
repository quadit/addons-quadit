# -*- coding: utf-8 -*-
# © <2016> <QuadIT>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class EmailTemplate(models.Model):

    _inherit = 'email.template'

    create_reservation = fields.Boolean()
    update_reservation = fields.Boolean()
