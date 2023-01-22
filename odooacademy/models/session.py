# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Session(models.Model):
    _name = 'odooacademy.session'
    _description = 'odooacademy.session'

    name = fields.Char('Name', required=True, index=True)
    course_id = fields.Many2one('odooacademy.course', string='Course')
    # user_id = fields.Many2one('res.users', string='Instructor', domain="[('is_instructor','=',True),('is_teacher','=',True)]")
    # user_id = fields.Many2one('res.users', string='Instructor', domain="['|',('is_instructor','=',True),('is_teacher','=',True)]")
    user_id = fields.Many2one('res.users', string='Instructor', domain="[('is_instructor','=',True)]")
    partner_ids = fields.Many2many('res.partner', string='Attendees')
    start_date = fields.Date('Start Date')
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
