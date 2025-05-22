# -*- coding: utf-8 -*-
from odoo import models, fields, api

#===========   This Model Create For Home/index page   ============
class Tourgull_visa(models.Model):
    _name = 'tourgull_visa.home'

    # For Slider
    slider = fields.Image(string='Slider Image')
    slider_image_url = fields.Char(string='Slider Image Url')
    slider_title = fields.Char(string='Slider Title')

    # For Video Slide
    is_video = fields.Boolean(string='Is Video?')
    video_file = fields.Binary(string='Video File')
    video_filename = fields.Char(string='Filename')

    # For ad 1
    ad1_image = fields.Image(string='Ad1 Image')
    ad1_image_url = fields.Char(string='Ad1 Image Url')
    ad1_title = fields.Char(string='Ad1 Title')
    ad1_description = fields.Char(string='Ad1 Description')
    ad1_url = fields.Char(string='Url')

    # For ad 2
    ad2_image = fields.Image(string='Ad2 Image')
    ad2_image_url = fields.Char(string='Ad2 Image Url')
    ad2_url = fields.Char(string='Url')

    # For filter section title and desc
    filter_section_title = fields.Char(string = 'Filter Section Title')
    filter_section_description = fields.Char(string = 'Filter Section Description')

    # For Country Info section title and desc
    country_info_title = fields.Char(string = 'Country Info Section Title')
    country_info_description = fields.Char(string = 'County Info Section Description')


    # For Offer Section Title and Desc
    offer_section_title = fields.Char(string='Offer Section Title')
    offer_section_description = fields.Char(string='Offer  Section Description')


    # For Suggest Service Section Title and Desc
    suggest_servie_section_title = fields.Char(string = 'Suggest Service Section Title')
    suggest_service_section_description = fields.Char(string = 'Suggest Service Section Description')

