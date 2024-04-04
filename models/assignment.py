from odoo import api, fields, models

class CompanyAssignment(models.Model):
    _name = 'company.assignment'
    _rec_name = 'car_id'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Company Assignment'


    car_id = fields.Many2one(comodel_name='company.car', string='Car', required=True)
    manufacturer = fields.Char(related='car_id.manufacturer', string='Manufacturer')
    model = fields.Char(related='car_id.model', string='Model')
    mileage = fields.Integer(related='car_id.mileage', string='Mileage')
    assignment_date = fields.Date(string='Assignment Date', default=fields.Date.context_today, required=True)
    end_assignment_date = fields.Date(string='End of Assignment')
    employee_id = fields.Many2one(comodel_name='company.employee', string='Employee', required=True)
    gender = fields.Selection(related='employee_id.gender', string='Gender', required=True)
    age = fields.Integer(related='employee_id.age', string='Age', required=True)
    driver_license = fields.Selection(related='employee_id.driver_license', string='Drivers License', required=True)

