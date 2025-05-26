# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request as req


class VisaInfo(http.Controller):
    @http.route('/visa/visa_info', auth='public', website=True)
    def visa_info(self, **kw):
        visa_data = req.env['tourgull_visa.visa_info'].sudo().search([], limit=1)
        suggest_slider = req.env['tourgull_visa.suggest_service_slider'].sudo().search([])
        category = req.env['tourgull_visa.category'].sudo().search([])
        country_info = req.env['tourgull_visa.country_info'].search([])

        return req.render('tourgull_visa.visa_info', {
            'visa_data': visa_data,
            'suggest_slider': suggest_slider,
            'category': category,
            'country_info': country_info,
            'search_data': kw  # 👈 Pass search data to template
        })

    # Contact Submit
    @http.route('/visa/contact_submit', type='http', auth='public', website=True, csrf=True)
    def contact_submit(self, **kw):
        description = kw.get('description', '').strip()

        req.env['tourgull_visa.contact'].create({
            'name': kw.get('name'),
            'email': kw.get('email'),
            'phone': kw.get('phone'),
            'description': description,
        })

        return req.redirect('/visa/visa_info')
