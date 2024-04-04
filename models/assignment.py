from odoo import api, fields, models

class CompanyAssignment(models.Model):
    _name = 'company.assignment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Company Assignment'

    car_id = fields.Many2one(comodel_name='company.car', string='Car', required=True)
