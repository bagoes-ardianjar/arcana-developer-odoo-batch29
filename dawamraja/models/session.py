from odoo import models, fields, api

class Session(models.Model):
    _name = 'dawamraja.session'
    _description = 'Session'

    name = fields.Char('Name', required=True, index=True)
    start_date = fields.Date('Start Date', default=fields.Date.today())
    duration = fields.Float('Duration')
    number_of_seats = fields.Float('Number Of Seats')
    description = fields.Text('Description')
    active = fields.Boolean('Active', default=True)

    course_id = fields.Many2one('dawamraja.course', string='Course')
    user_id = fields.Many2one('res.users', string='Instructor')
    partner_ids = fields.Many2many('res.partner', string='Attendees')

    taken_seats = fields.Float(string='Taken Seats', compute='_count_taken_seats', store=True)

    @api.depends('partner_ids','number_of_seats')
    def _count_taken_seats(self):
        for rec in self:
            if rec.partner_ids and rec.number_of_seats:
                rec.taken_seats = len(rec.partner_ids) / rec.number_of_seats * 100
            else:
                rec.taken_seats = 0
