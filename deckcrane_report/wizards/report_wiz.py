# -*- coding: utf-8 -*-

from datetime import datetime
from datetime import timedelta
from odoo import models, fields, api
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT as DATETIME_FORMAT
from dateutil.relativedelta import relativedelta


class PerformancyReportWizard(models.TransientModel):
    _name = 'performancy.report.wizard'

    date_start = fields.Date(string="Start Date", required=True, default=fields.Date.today)
    date_end = fields.Date(string="End Date", required=True, default=fields.Date.today)
    city_id = fields.Many2one('city',string="Home Base")

    @api.multi
    def get_report(self):
        """Call when button 'Get Report' clicked.
        """
        data = {
            'ids': self.ids,
            'model': self._name,
            'form': {
                'date_start': self.date_start,
                'date_end': self.date_end,
                'city_id': self.city_id.name,
            },
        }

        # use `module_name.report_id` as reference.
        # `report_action()` will call `_get_report_values()` and pass `data` automatically.
        return self.env.ref('deckcrane_report.performancy_report').report_action(self, data=data)


class ReportPerformancyReportView(models.AbstractModel):
    """
        Abstract Model specially for report template.
        _name = Use prefix `report.` along with `module_name.report_name`
    """
    _name = 'report.deckcrane_report.performancy_report_view'

    @api.model
    def _get_report_values(self, docids, data=None):
        date_start = data['form']['date_start']
        date_end = data['form']['date_end']
        city_id = data['form']['city_id']
        date_start_obj = datetime.strptime(date_start, DATE_FORMAT)
        date_end_obj = datetime.strptime(date_end, DATE_FORMAT)
        date_diff = (date_end_obj - date_start_obj).days + 1

        docs = []
        performancy = self.env['performancy.deck'].search([
            ('start_date', '>=', date_start_obj.strftime(DATETIME_FORMAT)),
            ('end_date', '<=', date_end_obj.strftime(DATETIME_FORMAT)),
        ])
        for pd in performancy:
            total = date_diff * 24
            total_dt = (pd.end_date - pd.start_date).days + 1
            avala = (total - total_dt)/total * 100
            docs.append({
                'name_of_ship': pd.name_of_ship,
                'crane_type': pd.crane_type,
                'city': pd.city,
                'total': total,
                'total_dt': total_dt,
                'avala': avala,
                'breakdown_condition': pd.breakdown_condition,
                'company': self.env.user.company_id
            })

        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'date_start': date_start,
            'date_end': date_end,
            'city_id':city_id,
            'docs': docs,
        }

