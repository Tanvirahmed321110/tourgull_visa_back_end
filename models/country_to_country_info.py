from odoo import models, fields, api

# ============  This Model Create For Country To Country Information  ============
class Tourgull_visa (models.Model):
    _name = 'tourgull_visa.con_to_con'

    # Many2one
    form = fields.Many2one('tourgull_visa.country' ,string='From Country')
    to = fields.Many2one('tourgull_visa.country', string='To Country')
    category_id = fields.Many2one('tourgull_visa.category',string='Visa Category')

    # come to country mode
    country_ids = fields.Many2many('tourgull_visa.country_info', string='Country Information')

    # Html fields for this model
    # information = fields.Html(string='Information')
    # process_time = fields.Html(string='Process Time')
    # faq = fields.Html(string='FAQ')
    # head_office_regional_office = fields.Html(string='Head_office Regional_office')
    # visa_free = fields.Html(string='Visa Free')
    # photo_specification = fields.Html(string='Photo Specificaiton')
