# -*- coding: utf-8 -*-
from odoo import models, fields, api

#===========   This Model Create For [all country] page   ============
class Tourgull_visa(models.Model):
    _name = 'tourgull_visa.continent'

    # For Slider
    name = fields.Char(string='Continent Name')



