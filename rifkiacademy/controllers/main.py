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

    @http.route('/index/courses/', auth='public')
    def courses(self, **kw):
        courses = http.request.env['rifkiacademy.course'].sudo().search([])
        return http.request.render('rifkiacademy.courses', {
            'courses': courses,
        })

    @http.route('/courses/', auth='public', website=True)
    def courses(self, **kw):
        courses = http.request.env['rifkiacademy.course'].sudo().search([])
        return http.request.render('rifkiacademy.course_websites', {
            'courses': courses,
        })