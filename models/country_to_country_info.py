from odoo import models, fields, api

# ============  This Model Create For Country To Country Information  ============
class Tourgull_visa (models.Model):
    _name = 'tourgull_visa.country_to_country_info'

    # Many2one
    form = fields.Many2one('tourgull_visa.country' ,string='From Country')
    to = fields.Many2one('tourgull_visa.country', string='To Country')
    category_id = fields.Many2one('tourgull_visa.category',string='Visa Category')

    # Html fields for this model
    information = fields.Html(string='Information')
    process_time = fields.Html(string='Process Time')
    faq = fields.Html(string='FAQ')
    head_office_regional_office = fields.Html(string='Head_office Regional_office')
    visa_free = fields.Html(string='Visa Free')
    photo_specification = fields.Html(string='Photo Specificaiton')
