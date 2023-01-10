#  -*- coding: utf-8 -*-
# Copyright 2023 Sodexis
#  Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = "account.move"


    payment_method_id = fields.Many2one(
        'account.journal',
        string='Payment Method',
        domain=[
            ('type', 'in', ['bank', 'cash'])
        ],
        copy=False,
    )

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        super()._onchange_partner_id()
        if self.partner_id.commercial_partner_id.purchase_payment_method_id:
            self.payment_method_id = self.partner_id.commercial_partner_id.purchase_payment_method_id.id
        elif self.partner_id.property_payment_method_id:
            self.payment_method_id = self.partner_id.purchase_payment_method_id.id
        else:
            self.payment_method_id = None