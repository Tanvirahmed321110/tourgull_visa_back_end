# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request as req

class AllCountryBlog(http.Controller):
    @http.route('/visa/all_country_blog', auth='public')
    def all_country_blog(self, **kw):
        return req.render('tourgull_visa.all_country_blog', {
            'root': 'aaaa',
        })
