from odoo import models, fields, api

class Session(models.Model):
    _name = 'dawamraja.session'
    _description = 'Session'

    name = fields.Char('Name', required=True, index=True)
    start_date = fields.Date('Start Date')
    duration = fields.Float('Duration')
    number_of_seats = fields.Float('Number Of Seats')
    description = fields.Text('Description')