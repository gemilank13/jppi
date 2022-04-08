# -*- coding: utf-8 -*-

from odoo import models, fields, api

class InspectLoc(models.Model):
    _name = 'inspect.loc'
    # _rec_name = 'asset_numb'
    # _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char('Location', required=True, copy=False)