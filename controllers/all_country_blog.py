# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request as req

class AllCountryBlog(http.Controller):
    @http.route('/visa/all_country_blog', auth='public')

    def all_country_blog(self, **kw):
        country_blog_data = req.env['tourgull_visa.all_country_blog'].search([])
        country = req.env['tourgull_visa.country'].sudo().search([])
        suggest_slider = req.env['tourgull_visa.suggest_service_slider'].sudo().search([])

        return req.render('tourgull_visa.all_country_blog', {
            'country_blog_data' :country_blog_data,
            'country' : country,
            'suggest_slider' :suggest_slider
        })
