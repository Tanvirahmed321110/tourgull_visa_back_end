# -*- coding: utf-8 -*-
from odoo import models, fields, api

#===========   This Model Create For [Tab and Information]    ============
class Tourgull_visa(models.Model):
    _name = 'tourgull_visa.country_info'

    # For Slider
    name = fields.Char(string='Tab Button Name' , required=True)
    description = fields.Html(string='Description' , required=True)



