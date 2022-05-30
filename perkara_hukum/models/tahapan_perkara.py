# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TahapanPerkara(models.Model):
    _name = 'tahapan.perkara'
    
    name = fields.Char(string="Tahapan Perkara")

