from datetime import date
from odoo import api, fields, models

class CompanyEmployee(models.Model):
    _name = 'company.employee'
    _rec_name = 'name'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Company Employee'

    name = fields.Char(string='Name', required=True)
    driver_license = fields.Selection([('yes', 'Yes'), ('no', 'No')], string='Driver License', required=True)
    email = fields.Char(string='Email', required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', required=True)
    date_of_birth = fields.Date(string='Date of Birth', required=True)
    age = fields.Integer(string='Age', required=True, compute='_compute_age', tracking=True)


    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age=1



