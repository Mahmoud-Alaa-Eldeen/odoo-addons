# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo Addon, Open Source Management Solution
#    Copyright (C) 2014-now Equitania Software GmbH(<http://www.equitania.de>).
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
##############################################################################

from openerp import models, fields, api, _
from openerp.exceptions import ValidationError


#aktuell noch auskommentiert; evtl. direkt ins oca-Modul oder dependency einbauen
# class hr_analytic_timesheet(models.Model):
#     _inherit = "hr.analytic.timesheet"
#
#     @api.constrains('aal_time_stop', 'aal_time_start')
#     def _check_time_input(self):
#         if self.aal_time_stop < 0 or self.aal_time_stop >= 24 or self.aal_time_start < 0 or self.aal_time_start >= 24:
#             raise ValidationError(_("Input for the time must be between 0 and 24 hours"))