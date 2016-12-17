# -*- coding: utf-8 -*-
# © <2016> <Quad IT>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class StockPickingMassive(models.Model):

    _name = 'stock.picking.massive'

    name = fields.Char(
        string='Name',
        default='/',
        required=True,)
    date = fields.Datetime(string='Datetime', required=True,)
    picking_type_id = fields.Many2one(
        comodel_name='stock.picking.type',
        string='Picking Type',
        required=True,)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], default='draft')
    location_id = fields.Many2one(
        comodel_name='stock.location',
        string='Location Origin',
        required=True,)
    location_dest_id = fields.Many2one(
        comodel_name='stock.location',
        string='Location Dest',
        required=True,)
    line_ids = fields.One2many(
        comodel_name='stock.picking.massive.line',
        inverse_name='mass_id',
        string='Lines')

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].get('stock.picking.massive')
        return super(StockPickingMassive, self).create(vals)

    @api.multi
    def action_cancelled(self):
        self.state = 'cancelled'

    @api.multi
    def action_create_pickings(self):
        move_ids = []
        for rec in self:
            picking_obj = self.env['stock.picking']
            for l in rec.line_ids:
                xline = (0, 0, {
                    'name': l.product_id.description or l.product_id.name,
                    'product_id': l.product_id.id,
                    'box': l.box,
                    'paperboard': l.paperboard,
                    'egg': l.egg,
                    'picking_type_id': rec.picking_type_id.id,
                    'product_uom': l.product_id.uom_id.id,
                    'location_id': rec.location_id.id,
                    'location_dest_id': rec.location_dest_id.id,
                })
                move_ids.append(xline)
            vals = {
                'picking_type_id': rec.picking_type_id.id,
                'date': rec.date,
                'move_lines': [x for x in move_ids],
                'origin': rec.name,
            }
            picking_id = picking_obj.create(vals)
            picking_id.action_confirm()
            picking_id.do_transfer()
            rec.state = 'done'


class StockPickingMssiveLine(models.Model):

    _name = 'stock.picking.massive.line'

    product_id = fields.Many2one(
        comodel_name='product.product',
        string='Product')
    egg = fields.Float(string='Eggs')
    box = fields.Float('Boxes')
    paperboard = fields.Float('Paperboard')
    mass_id = fields.Many2one(
        comodel_name='stock.picking.massive',
        string='Picking Massive')
