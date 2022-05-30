# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Lampiran(models.Model):
    _name = 'lampiran.lampiran'
    
    name = fields.Binary(string="Lampiran")
    perkara_hukum_id = fields.Many2one('perkara.hukum', readonly=True)