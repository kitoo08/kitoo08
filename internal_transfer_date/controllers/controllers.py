# -*- coding: utf-8 -*-
# from odoo import http


# class InternalTransferDate(http.Controller):
#     @http.route('/internal_transfer_date/internal_transfer_date/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/internal_transfer_date/internal_transfer_date/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('internal_transfer_date.listing', {
#             'root': '/internal_transfer_date/internal_transfer_date',
#             'objects': http.request.env['internal_transfer_date.internal_transfer_date'].search([]),
#         })

#     @http.route('/internal_transfer_date/internal_transfer_date/objects/<model("internal_transfer_date.internal_transfer_date"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('internal_transfer_date.object', {
#             'object': obj
#         })
