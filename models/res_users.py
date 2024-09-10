from odoo import models, fields, api
import secrets
from datetime import datetime, timedelta

class ResUsers(models.Model):
    _inherit = 'res.users'

    api_key = fields.Char(string='API Key', copy=False, readonly=True)
    api_key_expiration = fields.Datetime(string='API Key Expiration', copy=False, readonly=True)

    def action_generate_api_key(self):
        for user in self:
            api_key = secrets.token_urlsafe(32)
            expiration = datetime.now() + timedelta(days=30)
            user.write({
                'api_key': api_key,
                'api_key_expiration': expiration
            })
        return True

    def action_clear_api_key(self):
        for user in self:
            user.write({
                'api_key': False,
                'api_key_expiration': False
            })
        return True