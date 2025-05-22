# -*- coding: utf-8 -*-
from odoo import models, fields, api

#===========   This Model Create For [Visa Info] page   ============
class Tourgull_visa(models.Model):
    _name = 'tourgull_visa.visa_info'

    # For Slider
    slider_image = fields.Image(string='Slider Image' , required=True)
    slider_image_url = fields.Char(string='Slider Image Url')
    slider_title = fields.Char(string='Slider Title')

    # For Ad
    ad_image = fields.Image(string='Ad Image' )
    ad_image_url = fields.Char(string='Ad Image Url')

    # For Suggest Service Section Title and Desc
    suggest_servie_section_title = fields.Char(string='Suggest Service Section Title')
    suggest_service_section_description = fields.Char(string='Suggest Service Section Description')


