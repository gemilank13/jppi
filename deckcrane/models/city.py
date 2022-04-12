# -*- coding: utf-8 -*-

from odoo import models, fields, api

class City(models.Model):
    _name = 'city'
    # _rec_name = 'asset_numb'
    # _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char('City', required=True)