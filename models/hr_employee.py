# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class HrExtendEmployee(models.Model):
    _inherit = "hr.employee"
    _order = 'sequence'

    employee_no = fields.Char(string='Emploee Number', )
    card_no = fields.Char(string='Card Number', )
    personal_email = fields.Char(help="private_email in hr")
    tamin_number = fields.Char(help="Tamin Ejtemaee Number")
    sequence = fields.Integer(default=500)

    # Translation
    job_title = fields.Char(translate=True)


class HrExtendEmployeePublic(models.Model):
    _inherit = "hr.employee.public"

    employee_no = fields.Char(string='Employee Number', )
    card_no = fields.Char(string='Card Number', )
    personal_email = fields.Char(help="private_email in hr")



class HrExtendEmployeeResumeLine(models.Model):
    _inherit = "hr.resume.line"

    name = fields.Char(translate=True)
    description = fields.Text(translate=True)