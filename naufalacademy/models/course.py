# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'naufalacademy.course'
    _description = 'naufalacademy.course'

    name = fields.Char('Title', required=True, index=True)
    user_id = fields.Many2one('res.users', string='Responsible User')
    session_ids = fields.One2many('naufalacademy.session', 'course_id', string='Sessions')
    description = fields.Text('Description')
