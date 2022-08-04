# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CraneType(models.Model):
    _name = 'crane.type'
    # _rec_name = 'asset_numb'
    # _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char('Crane Type', required=True, copy=False)
    # inspect_loc_id = fields.Many2one('inspect.loc','Inspection Location')
    # city_id = fields.Many2one('city','City')
    # name_of_ship = fields.Char('Name of Ship')
    # imo_number = fields.Char('IMO Number')