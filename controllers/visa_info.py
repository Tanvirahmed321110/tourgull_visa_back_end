# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request as req

class VisaInfo(http.Controller):
    @http.route('/visa/visa_info', auth='public')
    def visa_info(self,**kw):
        return req.render('tourgull_visa.visa_info',{
            'root':'a'
        })