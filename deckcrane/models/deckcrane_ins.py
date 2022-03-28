# -*- coding: utf-8 -*-

from odoo import models, fields, api

class DeckcraneIns(models.Model):
    _name = 'deckcrane.ins'
    # _rec_name = 'asset_numb'
    # _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char('Number', required=True)
    inspect_loc_id = fields.Many2one('inspect.loc','Location', required=True)
    city_id = fields.Many2one('city','City', required=True)
    deckcrane_id = fields.Many2one('deckcrane','Deck Crane', required=True)
    inspect_date = fields.Date(string="Inspection Date")
    equip_desc = fields.Text(string="Equipment Description")
    equip_manufact = fields.Char(string="Equipment Manufacture")
    registration = fields.Char(string="Equipment ID / Registration")
    # name_of_ship = fields.Char('Name of Ship')
    # imo_number = fields.Char('IMO Number')
    general_con = fields.Selection([
        ('statisfactory', 'Statisfactory'),
        ('exellent', 'Exellent'),
        ('good', 'Good')
    ], string='General Safety Condition')
    problems_rep = fields.Char(string="Problems or Repairs Needed")
    repairs_main = fields.Selection([
        ('competed', 'Competed'),
        ('scheduled', 'Scheduled'),
        ('overdue', 'Overdue')
    ], string='General Safety Condition')
    photos = fields.Binary('Photos')
    attachment = fields.Binary('Attachment')
    ins_item_ids = fields.One2many('inspect.item', 'deckcrane_ins_id', string="Inspection Items")


class InspectItem(models.Model):
    _name = 'inspect.item'

    name = fields.Char('What to inspect/look for')
    ins_result = fields.Selection([
        ('good/present', 'Good/Present'),
        ('needs repair/not present', 'Needs Repair/Not Present'),
        ('n/a', 'N/a')
    ], string='Inspection Result')
    comment = fields.Char('Comment')
    deckcrane_ins_id = fields.Many2one('deckcrane.ins','Deck Crane Inspection', required=True)