from odoo import http


class Dawamraja(http.Controller):
    
    @http.route('/web', auth='public')
    def index(self, **kw):
        return "Hello, world"
    
    @http.route('/web/teachers/', auth='public')
    def index(self, **kw):
        return http.request.render('dawamraja.teachers', {
            'teachers': ["Ujang", "Budi", "Dedi"],
        })
    
    @http.route('/web/courses/', auth='public')
    def courses(self, **kw):
        courses = http.request.env['dawamraja.course'].sudo().search([])
        return http.request.render('dawamraja.courses', {
            'courses': courses,
        })
    
    @http.route('/courses/', auth='public', website=True)
    def courses(self, **kw):
        courses = http.request.env['dawamraja.course'].sudo().search([])
        return http.request.render('dawamraja.course_websites', {
            'courses': courses,
        })



