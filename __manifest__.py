# -*- coding: utf-8 -*-
{
    'name': "dh_powerbi",

    'summary': """
        Power BI integration with Odoo API 
    """,

    'description': """
        Power BI integration with Odoo API using API key authentication
    """,

    'author': "dinoherlambang",
    'website': "http://www.github.com/dinoherlambang",

    'category': 'Tools',
    'version': '13.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/res_users_views.xml',  # Add this line
      
    ],
}