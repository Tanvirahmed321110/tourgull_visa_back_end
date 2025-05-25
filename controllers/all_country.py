from odoo import http
from odoo.http import request as req

class allCountry(http.Controller):
    @http.route('/visa/all_country', auth='public')
    def all_country(self,**kw):
        all_country_data = req.env['tourgull_visa.all_country'].search([])
        continent = req.env['tourgull_visa.continent'].search([])
        categories = req.env['tourgull_visa.category'].search([])
        suggest_slider = req.env['tourgull_visa.suggest_service_slider'].search([])
        country = req.env['tourgull_visa.country'].search([])

        return req.render('tourgull_visa.all_country',{
            'all_country_data':all_country_data,
            'continent':continent,
            'categories':categories,
            'suggest_slider':suggest_slider,
            'country' : country
        })