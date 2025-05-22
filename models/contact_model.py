from odoo import models, fields, api

# ============  This Model Create For Contact Info Submit  ============
class Tourgull_visa (models.Model):
    _name = 'tourgull_visa.contact'


    name = fields.Char(string='Name')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    description = fields.Text(string='Description')
