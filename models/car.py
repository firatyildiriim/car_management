from odoo import api, fields, models

class CompanyCar(models.Model):
    _name = 'company.car'
    _description = 'Company Car'

    manufacturer = fields.Char(string='Manufacturer Name', required=True)
    model = fields.Char(string='Model Name', required=True)
    year = fields.Integer(string='Year', required=True)
    plate = fields.Char(string='Plate Number', required=True)
    mileage = fields.Float(string='Milage', required=True)
    last_milage = fields.Float(string='Last Milage', required=True)
    fuel_type = fields.Selection([('gas', 'Gasoline'), ('diesel', 'Diesel')], string='Fuel type', required=True)
    warranty = fields.Selection([('yes', 'Yes'), ('no', 'No')] , string='Warranty', required=True)
    buying_date = fields.Datetime(string='Buying Date', required=True)
    selling_date = fields.Datetime(string='Selling Date', required=False)
    price = fields.Float(string='Price', required=True)
    lastprice = fields.Float(string='Selling Price', required=False)
    color = fields.Char(string='Color', required=True)

