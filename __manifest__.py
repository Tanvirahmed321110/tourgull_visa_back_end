# -*- coding: utf-8 -*-
{
    'name': "Visa Module",

    'summary': """
        Tourgull Visa Module""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Abdur Razzak , Tanvir",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'as_rental', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'templates/index.xml',
        'templates/visa_info.xml',
        'templates/all_country.xml',
        'templates/all_country_blog.xml',
        'views/index_views.xml',
        'views/all_country_blog_view.xml',
        'views/visa_info_view.xml',
        'views/all_country_view.xml',
        'views/country_view.xml',
        'views/category_view.xml',
        'views/suggest_service_slider_view.xml',
        'views/offer_slider_view.xml',
        'views/country_to_country_info_view.xml',
        'views/contact_view.xml',
        'views/continent_view.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}