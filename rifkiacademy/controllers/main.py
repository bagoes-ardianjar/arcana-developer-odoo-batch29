from odoo import http


class rifkiacademy(http.Controller):
    @http.route('/index', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/index/teachers/', auth='public')
    def index(self, **kw):
        return http.request.render('rifkiacademy.teachers', {
            'teachers': ["Ujang", "Budi", "Dedi"],
        })