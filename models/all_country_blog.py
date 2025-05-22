# -*- coding: utf-8 -*-
from odoo import models, fields, api

#===========   This Model Create For all country blog page   ============
class Tourgull_visa(models.Model):
    _name = 'tourgull_visa.all_country_blog'

    # For Slider
    slider_image = fields.Image(string='Slider Image', required=True)
    slider_image_url = fields.Char(string='Slider Image Url')

    # For Sidebar Content
    slider_top_content_title = fields.Char(string='Slider Content Title')
    slider_top_content_description = fields.Char(string='Slider Content Description')

    # For All Country Section Title and Desc
    all_country_section_title = fields.Char(string='All Country Section Title')
    all_country_section_description = fields.Char(string='All Country Section Description')

    # For Suggest Service Section Title and Desc
    suggest_servie_section_title = fields.Char(string='Suggest Service Section Title')
    suggest_service_section_description = fields.Char(string='Suggest Service Section Description')