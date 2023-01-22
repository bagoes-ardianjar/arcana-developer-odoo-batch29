# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InheritUsers(models.Model):
    _inherit = 'res.users'

    is_instructor = fields.Boolean('Is Instructor')
    # is_teacher = fields.Boolean('Is Teacher')