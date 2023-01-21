# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'bagoesacademy.course'
    _description = 'bagoesacademy.course'

    name = fields.Char('Title', required=True)
    description = fields.Text('Description')
