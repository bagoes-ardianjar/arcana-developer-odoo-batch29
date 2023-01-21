from odoo import models, fields, api

class Course(models.Model):
    _name = 'dawamraja.course'
    _description = 'Course'

    name = fields.Char(string="Course Name", required=True)
    description = fields.Text(string="Description")