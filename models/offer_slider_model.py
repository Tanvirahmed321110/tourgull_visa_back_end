# -*- coding: utf-8 -*-
from odoo import models, fields, api

#===========   This Model Create For Offer Slider   ============
class Tourgull_visa(models.Model):
    _name = 'tourgull_visa.offer_slider'

    # For Category
    name = fields.Char(string='Offer Name', required=True)
    image_1920 = fields.Image(string='Offer Image', required=True)
    url = fields.Char(string='Url', required=True)


