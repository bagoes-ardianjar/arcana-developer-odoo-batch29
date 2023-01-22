# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Session(models.Model):
	_name = 'bagoesacademy.session'
	_description = 'bagoesacademy.session'

	name = fields.Char('Name', required=True, index=True)
	course_id = fields.Many2one('bagoesacademy.course', string='Course')
	# user_id = fields.Many2one('res.users', string='Instructor', domain="[('is_instructor','=',True),('is_teacher','=',True)]")
	# user_id = fields.Many2one('res.users', string='Instructor', domain="['|',('is_instructor','=',True),('is_teacher','=',True)]")
	partner_id = fields.Many2one('res.partner', string='Instructor', domain="[('is_instructor','=',True)]")
	partner_ids = fields.Many2many('res.partner', string='Attendees')
	start_date = fields.Date('Start Date', default=fields.Date.today())
	active = fields.Boolean('Active', default=True)
	duration = fields.Float('Duration')
	number_of_seats = fields.Float('Number Of Seats')
	description = fields.Text('Description')
	taken_seats = fields.Float(string='Taken Seats', compute='_count_taken_seats', store=True)

	@api.depends('partner_ids','number_of_seats')
	def _count_taken_seats(self):
		for rec in self:
			if rec.partner_ids and rec.number_of_seats:
				rec.taken_seats = len(rec.partner_ids) / rec.number_of_seats * 100
			else:
				rec.taken_seats = 0

	@api.onchange('number_of_seats','partner_ids')
	def _onchange_number_of_seats(self):
		if self.number_of_seats < 0:
			return {
						'warning': {
							'title': "Something bad happened",
							'message': "Invalid Value",
						}
					}
		if len(self.partner_ids) > self.number_of_seats:
			return {
						'warning': {
							'title': "Something bad happened",
							'message': "Participants more than {}".format(int(self.number_of_seats)),
						}
					}
		
		@api.constrains('partner_ids','partner_id')
		def check_attendees(self):
			for rec in self:
				if rec.partner_id in rec.partner_ids:
					raise ValidationError("Your attendess is instructor: %s" % rec.partner_id.name)