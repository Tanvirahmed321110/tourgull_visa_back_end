# -*- coding: utf-8 -*-
from odoo import models, fields, api

#===========   This Model Create For [Visa Info] page   ============
class Tourgull_visa(models.Model):
    _name = 'tourgull_visa.visa_info'

    # For Slider
    slider_image = fields.Image(string='Slider Image' , required=True)
    slider_image_url = fields.Char(string='Slider Image Url')

    # For Ad
    ad_image = fields.Image(string='Ad Image' )
    ad_image_url = fields.Char(string='Ad Image Url')



