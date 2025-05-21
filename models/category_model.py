# -*- coding: utf-8 -*-
from odoo import models, fields, api

#===========   This Model Create For Category   ============
class Tourgull_visa(models.Model):
    _name = 'tourgull_visa.category'

    # For Category
    name = fields.Char(string='Category', required=True)


