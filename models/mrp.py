# -*- coding: utf-8 -*-
###############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2017 Humanytek (<www.humanytek.com>).
#    Rubén Bravo <rubenred18@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from odoo import api, fields, models
import logging
_logger = logging.getLogger(__name__)


class MrpProduction(models.Model):
    _name = "mrp.production"
    _inherit = 'mrp.production'

    sale_type_id = fields.Char(related='sale_id.type_id.name',
                              string='Sale Order Type',
                              readonly=True, store=False)
    type_priority = fields.Integer(related='sale_id.type_id.priority',
                            string='Priority', readonly=True,
                            store=False)
    sale_line_observation = fields.Text('Observation',
                            compute='_compute_observation', readonly=True)

    @api.one
    def _compute_observation(self):
        productions = self.search([('sale_id', '=', self.sale_id.id)])
        cont = 0
        for production in productions:
            if production.id == self.id:
                break
            cont += 1
        if self.sale_id:
            self.sale_line_observation = self.sale_id.order_line[cont].observation

