# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request as req

class Visa(http.Controller):
    @http.route('/visa', auth='public')
    def home(self, **kw):
        return req.render('tourgull_visa.tourgull_visa', {
            'root': 'aaaa',
        })
