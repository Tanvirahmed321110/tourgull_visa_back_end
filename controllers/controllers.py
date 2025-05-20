# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request as req

class Visa(http.Controller):
    @http.route('/visa/test1', auth='public')
    def test1(self, **kw):
        return req.render('tourgull_visa.test1', {
            'root': 'aaaa',
        })
