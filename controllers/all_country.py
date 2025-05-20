from odoo import http
from odoo.http import request as req

class allCountry(http.Controller):
    @http.route('/visa/all_country', auth='public')
    def all_country(self,**kw):
        return req.render('tourgull_visa.all_country',{
            'root':'a'
        })