from odoo import http


class Odooacademy(http.Controller):
    
    @http.route('/index', auth='public')
    def index(self, **kw):
        return "Hello, world"
    
    @http.route('/index/teachers/', auth='public')
    def index(self, **kw):
        return http.request.render('odooacademy.teachers', {
            'teachers': ["Ujang", "Budi", "Dedi"],
        })