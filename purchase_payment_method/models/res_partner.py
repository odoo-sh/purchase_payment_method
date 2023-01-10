# Copyright 2023 Sodexis
# License OPL-1 (See LICENSE file for full copyright and licensing details).

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    purchase_payment_method_id = fields.Many2one(
        'account.journal',
        domain=[
            ('type', 'in', ['bank', 'cash'])
        ],
        string='Purchase Payment Method', copy=False,
    )
