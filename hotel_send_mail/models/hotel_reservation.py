# -*- coding: utf-8 -*-
# © <2017> <Quadit, S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, models


class HotelReservation(models.Model):

    _inherit = 'hotel.reservation'

    @api.model
    def create(self, values):
        res = super(HotelReservation, self).create(values)
        email_template_obj = self.env['email.template']
        template_ids = email_template_obj.search([
            ('model', '=', 'hotel.reservation'),
            ('create_reservation', '=', True),
        ], limit=1)
        if template_ids:
            vals = email_template_obj.generate_email(template_ids.id, res.id)
            mail_mail_obj = self.env['mail.mail']
            msg_id = mail_mail_obj.create(vals)
            msg_id.send()
        return res

    @api.multi
    def write(self, values):
        email_template_obj = self.env['email.template']
        template_ids = email_template_obj.search([
            ('model', '=', 'hotel.reservation'),
            ('update_reservation', '=', True),
        ], limit=1)
        if template_ids:
            vals = email_template_obj.generate_email(template_ids.id, self.id)
            mail_mail_obj = self.env['mail.mail']
            msg_id = mail_mail_obj.create(vals)
            msg_id.send()
        return super(HotelReservation, self).write(values)
