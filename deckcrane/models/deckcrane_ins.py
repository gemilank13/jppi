# -*- coding: utf-8 -*-

from odoo import models, fields, api

class DeckcraneIns(models.Model):
    _name = 'deckcrane.ins'
    # _rec_name = 'asset_numb'
    # _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char('Inspection Code', readonly=True, required=True, copy=False, default='New')
    deckcrane_id = fields.Many2one('deckcrane','Deck Crane', required=True)
    inspect_date = fields.Datetime(string="Inspection Date", required=True)
    inspect_status = fields.Selection([
        ('acceptable', 'Acceptable'),
        ('unacceptable', 'Unacceptable'),
        ('acceptable with review', 'Acceptable With Review'),
        ('undesirable', 'Undesirable'),
        ('needs further review', 'Needs Further Review, Not Acceptable'),
        ('n/a', 'N/A')
    ], string='Inspection Status', required=True)
    inspect_sch_status = fields.Selection([
        ('completed', 'Completed'),
        ('scheduled', 'Scheduled'),
        ('overdue', 'Overdue')
    ], string='Inspection Schedule Status', required=True)
    attachment = fields.Binary('Attachment')
    ins_item_ids = fields.One2many('inspect.item', 'deckcrane_ins_id', string="Inspection Items")
    notes = fields.Text('Notes')
    city = fields.Char('City' , related="deckcrane_id.city_id.name")


    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('self.deckcrane') or 'New'
        result = super(DeckcraneIns, self).create(vals)
        return result


class InspectItem(models.Model):
    _name = 'inspect.item'

    name = fields.Many2one('item', 'Inspection Item', required=True)
    photos = fields.Binary('Photos')
    ins_result = fields.Selection([
        ('good/present', 'Good/Present'),
        ('needs repair/not present', 'Needs Repair/Not Present'),
        ('n/a', 'N/a')
    ], string='Inspection Result')
    description = fields.Char('Description', required=True)
    recommen = fields.Char('Recommendation')
    deckcrane_ins_id = fields.Many2one('deckcrane.ins','Deck Crane Inspection')