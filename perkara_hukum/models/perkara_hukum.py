# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PerkaraHukum(models.Model):
    _name = 'perkara.hukum'
    
    name = fields.Char(string="Kode Perkara", readonly=True, required=True, copy=False, default='New')
    nomor_surat = fields.Char('Nomor Surat', required=True)
    tanggal = fields.Date('Tanggal', required=True)
    nama_perkara = fields.Char('Nama Perkara', required=True)
    klasifikasi_perkara_id = fields.Many2one('klasifikasi.perkara','Klasifikasi Perkara', required=True)
    # user_id = fields.Many2one('res.users', string='User', readonly=True ,default=lambda self: self.env.user)
    status_perkara = fields.Selection([ ('proses', 'Proses'),('selesai', 'Selesai'),],'Status Perkara', required=True)
    catatan = fields.Text('Catatan')
    tahapan_perkara_history_ids = fields.One2many('tahapan.perkara.history', 'perkara_hukum_id', string="Tahapan Perkara")
    lampiran_ids = fields.One2many('lampiran.lampiran', 'perkara_hukum_id', string="Lampiran")
    para_pihak_ids = fields.One2many('para.pihak', 'perkara_hukum_id', string="Para Pihak")


    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('self.perkara') or 'New'
        result = super(PerkaraHukum, self).create(vals)
        return result