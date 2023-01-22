# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Session(models.Model):
    _name = 'bagoesacademy.session'
    _description = 'bagoesacademy.session'

    name = fields.Char('Name', required=True, index=True)
    course_id = fields.Many2one('bagoesacademy.course', string='Course')
    user_id = fields.Many2one('res.users', string='Instructor')
    start_date = fields.Date('Start Date')
    duration = fields.Float('Duration')
    number_of_seats = fields.Float('Number Of Seats')
    description = fields.Text('Description')
