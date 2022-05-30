# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TahapanPerkaraHistory(models.Model):
    _name = 'tahapan.perkara.history'
    # _rec_name = 'date'
    
    tahapan_perkara_id = fields.Many2one('tahapan.perkara', 'Tahapan Perkara', required=True)
    tanggal = fields.Date('Tanggal', required=True)
    lampiran = fields.Binary('Lampiran', required=True)
    keterangan = fields.Char('Keterangan')
    status = fields.Selection([ ('proses', 'Proses'),('selesai', 'Selesai'),],'Status')
    perkara_hukum_id = fields.Many2one('perkara.hukum')