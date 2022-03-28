# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Deckcrane(models.Model):
    _name = 'deckcrane'
    # _rec_name = 'asset_numb'
    # _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char('Name of Ship', required=True)
    ship_type_id = fields.Many2one('jenis.kapal','Ship Type')
    imo_number = fields.Char('IMO Number')
    years_of_build = fields.Date('Years of Build')
    roll_up_load = fields.Char('Roll Up Load')
    roll_up_speed = fields.Char('Roll Up Speed')
    roll_down_speed = fields.Char('Roll Down Speed')
    swing_speed = fields.Char('Swing Speed')
    power_supply = fields.Char('Power Supply')
    photos = fields.Binary('Photos')