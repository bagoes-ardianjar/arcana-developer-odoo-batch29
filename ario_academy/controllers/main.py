from odoo import http


class Arioacademy(http.Controller):
    
    @http.route('/index', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/index/teachers/', auth='public')
    def index(self, **kw):
        return http.request.render('ario_academy.teachers', {
            'teachers': ["Ujang", "Budi", "Dedi"],
        })

    @http.route('/index/courses/', auth='public')
    def courses(self, **kw):
        courses = http.request.env['ario_academy.course'].sudo().search([])
        return http.request.render('ario_academy.courses', {
            'courses': courses,
        })



    @http.route('/url/<name>', auth='public', website=True)
    def url_name(self, name):
        return "<h1>{}</h1>".format(name)

    @http.route('/type/<int:id>', auth='public', website=True)
    def url_type(self, id):
        return '<h1>{} ({})</h1>'.format(id, type(id).__name__)


    @http.route('/courses/', auth='public', website=True)
    def courses(self, **kw):
        courses = http.request.env['ario_academy.course'].sudo().search([])
        return http.request.render('ario_academy.course_websites', {
            'courses': courses,
        })

    @http.route('/courses/<model("ario_academy.course"):course>/', auth='public', website=True)
    def course(self, course):
        return http.request.render('ario_academy.course', {
            'course': course
        })

    @http.route('/courses/add/', auth='public', website=True)
    def add(self, **kw):
        users = http.request.env['res.users'].sudo().search([])
        return http.request.render('ario_academy.add_course', {
            'users': users
        })
    
    @http.route('/course/do-add/', auth='public', website=True, method='POST')
    def do_add(self, **post):
        if post:
            vals = {
                'name' : post.get('name'),
                'user_id': post.get('user_id'),
                'description': post.get('description')
            }
            http.request.env['ario_academy.course'].sudo().create(vals)
        return http.request.redirect('/courses/')

    @http.route('/courses/edit/<int:id>/', auth='public', website=True)
    def edit(self, id):
        if id:
            course = http.request.env['ario_academy.course'].sudo().browse(int(id))
        users = http.request.env['res.users'].sudo().search([])
        return http.request.render('ario_academy.edit_course', {
            'course': course,
            'users': users
        })

    @http.route('/course/do-edit/', auth='public', website=True, method='POST')
    def do_edit(self, **post):
        if post.get('course_id'):
            course = http.request.env['ario_academy.course'].sudo().browse(int(post.get('course_id')))
            if course:
                vals = {
                    'name' : post.get('name'),
                    'user_id': post.get('user_id'),
                    'description': post.get('description')
                }
                course.sudo().write(vals)
        return http.request.redirect('/courses/')
    
    @http.route('/courses/delete/<int:id>/', auth='public', website=True)
    def delete(self, id):
        if id:
            course = http.request.env['ario_academy.course'].sudo().browse(int(id))
            if course:
                course.unlink()
        courses = http.request.env['ario_academy.course'].sudo().search([])
        return http.request.render('ario_academy.course_websites', {
            'courses': courses
        })