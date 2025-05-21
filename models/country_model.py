# -*- coding: utf-8 -*-
from odoo import models, fields, api

#===========   This Model Create For Country   ============
class Tourgull_visa(models.Model):
    _name = 'tourgull_visa.country'

    # For Country
    name = fields.Char(string='Country Name', required=True)
    image_1920 = fields.Image(string='Country Image', required=True)
    country_image_url = fields.Char(string='Country Image Url')


