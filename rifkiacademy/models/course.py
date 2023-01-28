# -*- coding: utf-8 -*-

from odoo import models, fields, api


class course(models.Model):
	_name = 'rifkiacademy.course'
	_description = 'rifkiacademy.course'

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
		return super(course, self).copy(default)

	name = fields.Char('Title', required=True, index=True,)
	user_id = fields.Many2one('res.users', string='Responsible User')
	session_ids = fields.One2many('rifkiacademy.session', 'course_id', string='Sessions')
	description = fields.Text('Description')

	# value = fields.Integer()
	# value2 = fields.Float(compute="_value_pc", store=True)

	# @api.depends('value')
	# def _value_pc(self):
	#     for record in self:
	#         record.value2 = float(record.value) / 100
