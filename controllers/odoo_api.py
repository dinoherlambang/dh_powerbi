from odoo import http
from odoo.http import request, Response
import json
import datetime
import logging

_logger = logging.getLogger(__name__)

class OdooAPI(http.Controller):
    @http.route('/api/data', type='http', auth='none', methods=['GET'], csrf=False)
    def get_data(self):
        headers = [('Content-Type', 'application/json')]
        try:
            _logger.info("Received request: %s", request.httprequest.headers)
            _logger.info("Params: %s", request.params)

            api_key = request.httprequest.headers.get('X-API-Key') or request.params.get('api_key')

            _logger.info("Extracted API Key: %s", api_key)

            if not api_key:
                _logger.error("API key is missing")
                return Response(json.dumps({'error': 'API key is missing'}), headers=headers, status=400)

            user = self.validate_api_key(api_key)
            if not user:
                _logger.error("Invalid or expired API key")
                return Response(json.dumps({'error': 'Invalid or expired API key'}), headers=headers, status=401)

            # Fetch and return data based on user permissions
            data = request.env['res.partner'].sudo().with_user(user).search_read([], ['name', 'email'])
            _logger.info("Data fetched successfully. Count: %s", len(data))
            return Response(json.dumps({'result': data}), headers=headers)
        except Exception as e:
            _logger.error("Unexpected error: %s", str(e), exc_info=True)
            return Response(json.dumps({'error': str(e)}), headers=headers, status=500)

    def validate_api_key(self, api_key):
        if not api_key:
            return None
        user = request.env['res.users'].sudo().search([('api_key', '=', api_key)], limit=1)
        if user and user.api_key_expiration > datetime.datetime.now():
            _logger.info("API key validated for user: %s", user.name)
            return user
        _logger.warning("Invalid API key or expired key")
        return None

    @http.route('/api/test', type='http', auth='none', methods=['GET'], csrf=False)
    def test_api(self):
        headers = [('Content-Type', 'application/json')]
        return Response(json.dumps({'status': 'API is working'}), headers=headers)