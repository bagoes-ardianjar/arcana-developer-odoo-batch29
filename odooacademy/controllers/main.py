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

    @http.route('/index/courses/', auth='public')
    def courses(self, **kw):
        courses = http.request.env['odooacademy.course'].sudo().search([])
        return http.request.render('odooacademy.courses', {
            'courses': courses,
        })

    @http.route('/courses/', auth='public', website=True)
    def courses(self, **kw):
        courses = http.request.env['odooacademy.course'].sudo().search([])
        return http.request.render('odooacademy.course_websites', {
            'courses': courses,
        })
    
    @http.route('/url/<name>', auth='public', website=True)
    def url_name(self, name):
        return "<h1>{}</h1>".format(name)