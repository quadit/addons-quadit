# -*- coding: utf-8 -*-
# © <2016> <QuadIT>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "QuadIT - Hotel Reservation Send Mail",
    "summary": "This module send mail when create or update hotel reservation",
    "author": "QuadIT",
    "website": "https://www.quadit.mx",
    "category": "Hidden",
    "version": "0.1",
    "depends": [
        "base",
        "email_template",
        "hotel_reservation",
        "quadit_hotel",
        "quadit_hotel_contract",
        "quadit_hotel_reservation_payment",
        "hotel_reservationfilter_gsisa",
    ],
    "application": True,
    "installable": True,
    "data": [
        "views/email_template_view.xml",
    ],
}
