# Copyright 2023 Sodexis
# License OPL-1 (See LICENSE file for full copyright and licensing details).

{
    'name': "Purchase Payment Method ",
    'summary': """Adds the payment method on the Customer and the Purchase Order. """,
    'version': "15.0.1.0.0",
    'category': 'Sale',
    'website': "http://sodexis.com/",
    'author': "Sodexis",
    'license': 'OPL-1',
    'installable': True,
    'application': False,
    'depends': [
        'account',
        'account_check_printing',
        'purchase',
    ],
    'data': [
        'views/purchase_view.xml',
        'views/res_partner_view.xml',
        'views/account_move_view.xml',
    ],
    'images': ['images/main_screenshot.png'],
    'cloc_exclude': [
        "**/*", # can be used to ignore an entire module.
    ],
}
