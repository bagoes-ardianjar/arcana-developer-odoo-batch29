# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'odooacademy.course'
    _description = 'odooacademy.course'

    _sql_constraints = [
		('check_name_description_different','CHECK (name != description)','Name and description must be different'),
		('check_name_unique','UNIQUE(name)','Name must be unique')
	]
    
    name = fields.Char('Title', required=True, index=True)
    user_id = fields.Many2one('res.users', string='Responsible User')
    session_ids = fields.One2many('odooacademy.session', 'course_id', string='Sessions')
    description = fields.Text('Description')
