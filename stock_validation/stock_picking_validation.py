# Copyright 2019 Quadit, S.A. de C.V. - https://www.quadit.mx
# Copyright 2019 Quadit (Gabriel López <Developer>)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).


from odoo import api, fields, models, _
from odoo.tools.float_utils import float_compare, float_is_zero
from odoo.exceptions import UserError, ValidationError


class StockPicking(models.Model):
    _inherit = "stock.picking"

    is_validate = fields.Boolean(string='Validate')

    @api.multi
    def button_validate(self):
        self.ensure_one()
        if not self.is_validate:
            raise ValidationError(
                _('There is no permission to validate the transfer.'))
        else:
            if not self.move_lines and not self.move_line_ids:
                raise UserError(_('Please add some items to move.'))

            # If no lots when needed, raise error
            picking_type = self.picking_type_id
            precision_digits = self.env['decimal.precision'].precision_get(
                'Product Unit of Measure')
            no_quantities_done = all(float_is_zero(move_line.qty_done, precision_digits=precision_digits)  # noqa
                                     for move_line in self.move_line_ids.filtered(lambda m: m.state not in ('done', 'cancel')))  # noqa
            no_reserved_quantities = all(float_is_zero(
                move_line.product_qty, precision_rounding=move_line.product_uom_id.rounding) for move_line in self.move_line_ids)  # noqa
            if no_reserved_quantities and no_quantities_done:
                raise UserError(
                    _('You cannot validate a transfer if no quantites are '
                      'reserved nor done. To force the transfer, switch in '
                      'edit more and encode the done quantities.'))

            if picking_type.use_create_lots or picking_type.use_existing_lots:
                lines_to_check = self.move_line_ids
                if not no_quantities_done:
                    lines_to_check = lines_to_check.filtered(
                        lambda line: float_compare(line.qty_done, 0,
                                                   precision_rounding=line.product_uom_id.rounding)  # noqa
                    )

                for line in lines_to_check:
                    product = line.product_id
                    if product and product.tracking != 'none':
                        if not line.lot_name and not line.lot_id:
                            raise UserError(
                                _('You need to supply a Lot/Serial number for product %s.') % product.display_name)  # noqa

            if no_quantities_done:
                view = self.env.ref('stock.view_immediate_transfer')
                wiz = self.env['stock.immediate.transfer'].create(
                    {'pick_ids': [(4, self.id)]})
                return {
                    'name': _('Immediate Transfer?'),
                    'type': 'ir.actions.act_window',
                    'view_type': 'form',
                    'view_mode': 'form',
                    'res_model': 'stock.immediate.transfer',
                    'views': [(view.id, 'form')],
                    'view_id': view.id,
                    'target': 'new',
                    'res_id': wiz.id,
                    'context': self.env.context,
                }

            if self._get_overprocessed_stock_moves() and not self._context.get('skip_overprocessed_check'):  # noqa
                view = self.env.ref('stock.view_overprocessed_transfer')
                wiz = self.env['stock.overprocessed.transfer'].create(
                    {'picking_id': self.id})
                return {
                    'type': 'ir.actions.act_window',
                    'view_type': 'form',
                    'view_mode': 'form',
                    'res_model': 'stock.overprocessed.transfer',
                    'views': [(view.id, 'form')],
                    'view_id': view.id,
                    'target': 'new',
                    'res_id': wiz.id,
                    'context': self.env.context,
                }

            # Check backorder should check for other barcodes
            if self._check_backorder():
                return self.action_generate_backorder_wizard()
            self.action_done()
            return
