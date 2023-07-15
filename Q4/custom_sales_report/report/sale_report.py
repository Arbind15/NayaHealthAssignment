# report.py

from odoo import models, api


class CustomSalesReport(models.AbstractModel):
    _name = 'report.custom_sales_report.report_custom_sales'
    _description = 'Sales Report'

    @api.model
    def render_html(self, docids, data=None):
        report_obj = self.env['report']
        invs_obj = self.env['account.invoice.line']
        customer_id = data['form']['customer_id']
        from_date = data['form']['from_date']
        to_date = data['form']['to_date']
        invs = invs_obj.search([('partner_id', '=', customer_id),
                                ('create_date', '>=', from_date),
                                ('create_date', '<=', to_date)])
        # return {
        #     'docs': sales,
        # }
        name = self.env['res.partner'].browse(customer_id).name

        total = 0.0
        for inv in invs:
            total += inv.price_unit * inv.quantity
        return self.env['report'].render('custom_sales_report.'
                                         'report_custom_sales',
                                         {'docs': invs, 'total': total, 'name': name, 'from_date': from_date,
                                          'to_date': to_date})
