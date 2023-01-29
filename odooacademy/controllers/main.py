from odoo import http


class Odooacademy(http.Controller):
    
    @http.route('/index', auth='public')
    def index(self, **kw):
        return "Hello, world"