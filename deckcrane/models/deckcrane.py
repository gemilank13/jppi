# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Deckcrane(models.Model):
    _name = 'deckcrane'
    # _rec_name = 'asset_numb'
    # _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char('Name of Ship', required=True)
    ship_type_id = fields.Many2one('jenis.kapal','Ship Type', required=True)
    imo_number = fields.Char('IMO Number')
    years_of_build = fields.Date('Years of Build', required=True)
    roll_up_load = fields.Char('Roll Up Load')
    roll_up_speed = fields.Char('Roll Up Speed')
    roll_down_speed = fields.Char('Roll Down Speed')
    swing_speed = fields.Char('Swing Speed')
    power_supply = fields.Char('Power Supply')
    photos = fields.Binary('Photos')
    inspect_loc_id = fields.Many2one('inspect.loc','Location', required=True)
    city_id = fields.Many2one('city','City', required=True)
    ship_manufacture = fields.Char('Ship Manufacturer', required=True)
    ship_code = fields.Char(string="Ship Code", readonly=True, required=True, copy=False, default='New')

    @api.model
    def create(self, vals):
        if vals.get('ship_code', 'New') == 'New':
            vals['ship_code'] = self.env['ir.sequence'].next_by_code('self.service') or 'New'
        result = super(Deckcrane, self).create(vals)
        return result