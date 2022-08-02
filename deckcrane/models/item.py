# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Item(models.Model):
    _name = 'item'
    # _rec_name = 'asset_numb'
    # _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char('Inspection Item', required=True, copy=False)