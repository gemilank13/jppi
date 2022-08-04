# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PerformancyDeck(models.Model):
    _name = 'performancy.deck'
    # _rec_name = 'asset_numb'
    # _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char('Performancy Code', readonly=True, required=True, copy=False, default='New')
    deckcrane_id = fields.Many2one('deckcrane','Deck Crane', required=True)
    inspect_date = fields.Datetime(string="Inspection Date", required=True)
    name_of_ship = fields.Char('Name of Ship' , related="deckcrane_id.name" , store=True)
    crane_type = fields.Char('Crane Type' , related="deckcrane_id.crane_type_id.name" , store=True)
    city = fields.Char('City' , related="deckcrane_id.city_id.name" , store=True)
    location = fields.Char('Location' , related="deckcrane_id.inspect_loc_id.name" , store=True)
    ship_type = fields.Char('Ship Type' , related="deckcrane_id.ship_type_id.name" , store=True)
    condition_deck = fields.Selection([
        ('operation', 'Operation'),
        ('need for more inspection', 'Need For More Inspection'),
        ('not operation', 'Not Operation')
    ], string='Condition of Deckcrane', required=True)
    breakdown_condition = fields.Text(string= "Breakdown Condition Couse")
    start_date = fields.Datetime(string="Start Date", required=True)
    end_date = fields.Datetime(string="End Date", required=True)

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('self.performancy') or 'New'
        result = super(PerformancyDeck, self).create(vals)
        return result
