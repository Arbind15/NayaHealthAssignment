from odoo import models, fields, api


class GenerateSalesReportWizard(models.TransientModel):
    _name = 'generate.sales.report.wizard'
    _description = 'Generate Sales Report Wizard'

    from_date = fields.Date(string='From Date', required=True)
    to_date = fields.Date(string='To Date', required=True)
    customer_id = fields.Many2one('res.partner', string='Customer')

    @api.multi
    def generate_report(self):
        data = {
            'ids': self._ids,
            'model': 'custom.sales.report',
            'form': {
                'from_date': self.from_date,
                'to_date': self.to_date,
                'customer_id': self.customer_id.id,
            },
        }
        # return self.env.ref('custom_sales_report.action_report_custom_sales').report_action(self, data=data)
        return self.env['report'].get_action(self, 'custom_sales_report.'
                                                   'report_custom_sales',
                                             data=data)

