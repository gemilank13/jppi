# -*- coding: utf-8 -*-

from odoo import models, fields, api

class KlasifikasiPerkara(models.Model):
    _name = 'klasifikasi.perkara'
    
    name = fields.Char('Klasifikasi Perkara')