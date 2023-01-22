from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Course(models.Model):
    _name = 'dawamraja.course'
    _description = 'Course'

    name = fields.Char(string="Course Name", required=True)
    description = fields.Text(string="Description")

    user_id = fields.Many2one('res.users', string='Responsible User')
    session_ids = fields.One2many('dawamraja.session', 'course_id', string='Sessions')

    # SQL Constraints validation unique
    # _sql_constraints = [('name_unique', 'UNIQUE(name)', 'Course name must be unique')]

    # Python Constraints validation unique
    @api.constrains('name')
    def _check_name_unique(self):
        if self.search([('name', '=', self.name), ('id', '!=', self.id)]):
            raise ValidationError("Course Name must be unique")