# -*- coding: utf-8 -*-
from odoo import models, fields, api

#===========   This Model Create For Home/index page   ============
class Tourgull_visa(models.Model):
    _name = 'tourgull_visa.home'

    # For Slider
    slider = fields.Image(string='Slider Image', required=True)
    slider_image_url = fields.Char(string='Slider Image Url')

    # For ad 1
    ad1_image = fields.Image(string='Ad1 Image')
    ad1_image_url = fields.Char(string='Ad1 Image Url')
    ad1_title = fields.Char(string='Ad1 Title')
    ad1_description = fields.Char(string='Ad1 Description')

    # For ad 2
    ad2_image = fields.Image(string='Ad2 Image')
    ad2_image_url = fields.Char(string='Ad2 Image Url')
