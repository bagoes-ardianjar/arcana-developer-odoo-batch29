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
        
    def copy(self, default=None):
        # import pdb;
        # pdb.set_trace()
        # []
        default = dict(default or {}) 

        # Training Odoo
        # Cari course name nya like Copy of Training odoo
        # 3    
        copied_count = self.search_count(
            [('name', '=like', "Copy of {}%".format(self.name))])
        
        # Kalau tidak ada
        if not copied_count:
            # Copy of training odoo
            new_name = "Copy of {}".format(self.name)
        
        # # Kalau ada
        else:
            # Copy of training odoo (jumlah ada berapa)
            new_name = "Copy of {} ({})".format(self.name, copied_count)

        default['name'] = new_name
        return super(Course, self).copy(default)