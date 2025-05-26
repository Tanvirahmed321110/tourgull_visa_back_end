# controllers/visa.py
# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request as req
import base64
from server.odoo.addons.test_convert.tests.test_env import record


class Visa(http.Controller):

    @http.route('/visa', auth='public', website=True)
    def home(self, **kw):
        # Fetch data
        home_data = req.env['tourgull_visa.home'].sudo().search([], limit=1)
        categories  = req.env['tourgull_visa.category'].sudo().search([])
        offer_slider = req.env['tourgull_visa.offer_slider'].sudo().search([])
        country = req.env['tourgull_visa.country'].sudo().search([])
        suggest_slider = req.env['tourgull_visa.suggest_service_slider'].sudo().search([])

        # Prepare video source URL for direct embedding
        video_source = None
        if home_data.video_file:
            video_source = f"data:video/mp4;base64,{home_data.video_file}"
        elif home_data.video_url:
            video_source = home_data.video_url

        return req.render('tourgull_visa.tourgull_visa', {
            'home_data': home_data,
            'categories': categories,
            'offer_slider': offer_slider,
            'country': country,
            'suggest_slider': suggest_slider,
            'video_source' : video_source
        })

