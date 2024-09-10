from odoo import http
from odoo.http import request
import json
import datetime

class OdooAPI(http.Controller):
    @http.route('/api/data', type='json', auth='none')
    def get_data(self, api_key):
        user = self.validate_api_key(api_key)
        if not user:
            return {'error': 'Invalid or expired API key'}

        # Fetch and return data based on user permissions
        # This is an example, adjust according to your needs
        data = request.env['res.partner'].sudo().with_user(user).search_read([], ['name', 'email'])
        return {'data': data}

    def validate_api_key(self, api_key):
        user = request.env['res.users'].sudo().search([('api_key', '=', api_key)], limit=1)
        if user and user.api_key_expiration > datetime.datetime.now():
            return user
        return None