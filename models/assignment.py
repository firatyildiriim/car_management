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
    assignment_date = fields.Date(string='Assignment Date', default=fields.Date.context_today, required=True, tracking=True)
    end_assignment_date = fields.Date(string='End of Assignment', tracking=True)
    employee_id = fields.Many2one(comodel_name='company.employee', string='Employee', required=True)
    gender = fields.Selection(related='employee_id.gender', string='Gender', required=True)
    age = fields.Integer(related='employee_id.age', string='Age', required=True)
    driver_license = fields.Selection(related='employee_id.driver_license', string='Drivers License', required=True)
    active = fields.Boolean(string='Archieve', default=True, tracking=True)
    receipt = fields.Html(string='Receipt')
    note = fields.Text(string='Note')
    priority = fields.Selection([('0', 'Normal'), ('1', 'Low'), ('2', 'High'), ('3', 'Very High')], string='Priority')
    state = fields.Selection([('waiting', 'Waiting for Assignment'), ('in_process', 'In Assignment Process'), ('assigned', 'Assigned'), ('cancelled', 'Cancelled')], default ='waiting' ,string='Status')

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancelled'

    def action_waiting(self):
        for rec in self:
            rec.state = 'waiting'

    def action_process(self):
        for rec in self:
            rec.state = 'in_process'

    def action_assigned(self):
        for rec in self:
            rec.state = 'assigned'
