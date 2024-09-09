# -*- coding: utf-8 -*-
# from odoo import http


# class DhPowerbi(http.Controller):
#     @http.route('/dh_powerbi/dh_powerbi/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dh_powerbi/dh_powerbi/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dh_powerbi.listing', {
#             'root': '/dh_powerbi/dh_powerbi',
#             'objects': http.request.env['dh_powerbi.dh_powerbi'].search([]),
#         })

#     @http.route('/dh_powerbi/dh_powerbi/objects/<model("dh_powerbi.dh_powerbi"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dh_powerbi.object', {
#             'object': obj
#         })
