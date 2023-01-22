# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
	_name = 'dudenacademy.course'
	_description = 'dudenacademy.course'
	
	_sql_constraints = [
		('check_name_description_different','CHECK (name != description)','Name and description must be different'),
		('check_name_unique','UNIQUE(name)','Name must be unique')
	]
	
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


	name = fields.Char('Title', required=True)
	user_id = fields.Many2one('res.users', string='Responsible User')
	session_ids = fields.One2many('dudenacademy.session', 'course_id', string='Sessions')
	description = fields.Text('Description')
