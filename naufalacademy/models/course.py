# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'naufalacademy.course'
    _description = 'naufalacademy.course'

    name = fields.Char('Title', required=True)
    description = fields.Text('Description')
