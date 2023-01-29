from odoo import http


class rifkiacademy(http.Controller):
    @http.route('/index', auth='public')
    def index(self, **kw):
        return "Hello, world"