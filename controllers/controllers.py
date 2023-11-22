# -*- coding: utf-8 -*-
# from odoo import http


# class Sitecnet(http.Controller):
#     @http.route('/sitecnet/sitecnet', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sitecnet/sitecnet/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sitecnet.listing', {
#             'root': '/sitecnet/sitecnet',
#             'objects': http.request.env['sitecnet.sitecnet'].search([]),
#         })

#     @http.route('/sitecnet/sitecnet/objects/<model("sitecnet.sitecnet"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sitecnet.object', {
#             'object': obj
#         })
