from odoo import api, fields, models

class CompanyCar(models.Model):
    _name = 'company.car'
    _rec_name = 'plate'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Company Car'

    manufacturer = fields.Char(string='Manufacturer Name', required=True)
    model = fields.Char(string='Model Name', required=True, tracking=True)
    year = fields.Char(string='Year', required=True)
    plate = fields.Char(string='Plate Number', required=True, tracking=True)
    mileage = fields.Integer(string='Mileage(km)', required=True, tracking=True)
    engine_power = fields.Char(string='Engine Power', required=True)
    fuel_type = fields.Selection([('gas', 'Gasoline'), ('diesel', 'Diesel')], string='Fuel type', required=True)
    warranty = fields.Selection([('yes', 'Yes'), ('no', 'No')] , string='Warranty', required=True)
    buying_date = fields.Datetime(string='Buying Date', required=True)
    selling_date = fields.Datetime(string='Selling Date', required=False)
    price = fields.Integer(string='Price', required=True)
    lastprice = fields.Integer(string='Selling Price', required=False)
    color = fields.Char(string='Color', required=True)
    transmission = fields.Selection([('automatic', 'Automatic'), ('manuel', 'Manuel')] , string='Transmission', required=True)
    active = fields.Boolean(string='Active', default=True)

