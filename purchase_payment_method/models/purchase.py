# Copyright 2023 Sodexis
# License OPL-1 (See LICENSE file for full copyright and licensing details).

from odoo import models, api, fields, _


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    payment_method_id = fields.Many2one(
        'account.journal',
        domain=[('type', 'in', ['bank', 'cash'])],
        string='Payment Method',
    )

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        res = super(PurchaseOrder, self).onchange_partner_id()
        if self.partner_id.commercial_partner_id.purchase_payment_method_id:
            self.payment_method_id = self.partner_id.commercial_partner_id.purchase_payment_method_id.id
        elif self.partner_id.property_payment_method_id:
            self.payment_method_id = self.partner_id.purchase_payment_method_id.id
        else:
            self.payment_method_id = None
        return res

    def _prepare_invoice(self):
        invoice_vals = super()._prepare_invoice()
        if self.payment_method_id:
            invoice_vals.update({'payment_method_id': self.payment_method_id.id})
        return invoice_vals
