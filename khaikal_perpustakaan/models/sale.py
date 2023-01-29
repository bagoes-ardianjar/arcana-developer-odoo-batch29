from odoo import models, fields, api


class InheriSale(models.Model):
    _inherit = 'sale.order'

    tanggal_cetak = fields.Date(string='Tanggal Cetak')
    
    def test(self):
        return {
            'type': 'ir.actions.act_url',
            'url': 'https://www.google.com',
            'target': 'new'
        }