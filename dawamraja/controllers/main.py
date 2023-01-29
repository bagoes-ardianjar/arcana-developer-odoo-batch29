from odoo import http


class Dawamraja(http.Controller):
    
    @http.route('/index', auth='public')
    def index(self, **kw):
        return "Hello, world"
    
    @http.route('/index/teachers/', auth='public')
    def index2(self, **kw):
        return http.request.render('dawamraja.teachers', {
            'teachers': ["Ujang", "Budi", "Dedi"],
        })
    
    @http.route('/index/courses/', auth='public')
    def courses(self, **kw):
        courses = http.request.env['dawamraja.course'].sudo().search([])
        return http.request.render('dawamraja.courses', {
            'courses': courses,
        })
    
    @http.route('/courses/', auth='public', website=True)
    def courses2(self, **kw):
        courses = http.request.env['dawamraja.course'].sudo().search([])
        return http.request.render('dawamraja.course_websites', {
            'courses': courses,
        })
    
    @http.route('/courses/edit/<model("dawamraja.course"):course>/', auth='public', website=True)
    def edit(self, course):
        return http.request.render('dawamraja.edit_course', {
            'course': course
        })
    
    @http.route('/courses/delete/<int:id>/', auth='public', website=True)
    def delete(self, id):
        if id:
            course = http.request.env['dawamraja.course'].sudo().browse(int(id))
            if course:
                course.unlink()
        courses = http.request.env['dawamraja.course'].sudo().search([])
        return http.request.render('dawamraja.course_websites', {
            'courses': courses
        })

    
    @http.route('/url/<name>', auth='public', website=True)
    def url_name(self, name):
        return "<h1>{}</h1>".format(name)
    
    @http.route('/type/<int:id>', auth='public', website=True)
    def url_type(self, id):
        return '<h1>{} ({})</h1>'.format(id, type(id).__name__)
    
    @http.route('/courses/<model("dawamraja.course"):course>/', auth='public', website=True)
    def course(self, course):
        return http.request.render('dawamraja.course', {
            'course': course
        })






