# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ParaPihak(models.Model):
    _name = 'para.pihak'
    
    name = fields.Char(string="Para Pihak")
    perkara_hukum_id = fields.Many2one('perkara.hukum', readonly=True)