# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request as req

class Visa(http.Controller):
    @http.route('/visa', auth='public')
    def home(self, **kw):
        home_data = req.env['tourgull_visa.home'].sudo().search([],limit=1)
        categories = req.env['tourgull_visa.category'].sudo().search([])
        offer_slider = req.env['tourgull_visa.offer_slider'].sudo().search([])
        country = req.env['tourgull_visa.country'].sudo().search([])
        suggest_slider = req.env['tourgull_visa.suggest_service_slider'].sudo().search([])

        print('home_data', home_data)

        return req.render('tourgull_visa.tourgull_visa', {
            'home_data': home_data,
            'categories':categories,
            'offer_slider': offer_slider,
            'country': country,
            'suggest_slider': suggest_slider,
        })
