# -*- coding: utf-8 -*-
from odoo import models, fields, api


# ===========   This Model Create For Suggest Service Slider   ============
class Tourgull_visa(models.Model):
    _name = 'tourgull_visa.suggest_service_slider'

    # For Suggest Service
    name = fields.Char(string='Service Name', required=True)
    image_1920 = fields.Image(string='Service Image', required=True)
    url = fields.Char(string='Url')
