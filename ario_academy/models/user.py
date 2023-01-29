from odoo import models, fields, api

class InheritUsers(models.Model):
    _inherit = 'res.users'
    is_instructor = fields.Boolean(string='Is Instuctor')
    
   
    
