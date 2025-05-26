# controllers/visa.py
# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request as req


class Visa(http.Controller):

    @http.route('/visa', auth='public', website=True)
    def home(self, **kw):
        # Fetch data
        home_data = req.env['tourgull_visa.home'].sudo().search([], limit=1)
        categories  = req.env['tourgull_visa.category'].sudo().search([])
        offer_slider = req.env['tourgull_visa.offer_slider'].sudo().search([])
        country = req.env['tourgull_visa.country'].sudo().search([])
        suggest_slider = req.env['tourgull_visa.suggest_service_slider'].sudo().search([])

        # Build dictionary of category_id: country list
        # category_countries = {}
        # for item in categories:
        #     countries = req.env['tourgull_visa.country'].sudo().search([
        #         ('categories', 'in', [item.id])
        #     ])
        #     category_countries[item.id] = countries
        student_countries = req.env['tourgull_visa.country'].sudo().search([
            ('categories.name', '=', 'Tourist')
        ])
        tourist_countries = req.env['tourgull_visa.country'].sudo().search([
            ('categories.name', '=', 'tourist')
        ])
        visa_countries = req.env['tourgull_visa.country'].sudo().search([
            ('categories.name', '=', 'visa')
        ])

        return req.render('tourgull_visa.tourgull_visa', {
            'home_data': home_data,
            'categories': categories,
            'offer_slider': offer_slider,
            'country': country,
            'suggest_slider': suggest_slider,
            'category_countries': category_countries
        })
