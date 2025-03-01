# -*- coding: utf-8 -*-
{
    'name': "QR CODE SCANNER",
    'summary': "QR CODE SCANNER",
    'description': """
QR CODE SCANNER Module for scanning QR codes and integrating with Odoo Inventory and Partners.
    """,
    'category': 'Inventory/Inventory',
    'sequence': 100,
    'version': '1.0',
    'depends': ['base', 'stock', 'web_tour'],
    'data': [
        # Security Access (if required)
        # 'security/ir.model.access.csv',

        # Views
        'views/views.xml',
        'views/res_partner_inheirt_view.xml',
        # 'views/stock_picking_views.xml',
        # 'views/stock_move_line_views.xml',
        # 'views/stock_barcode_views.xml',
        # 'views/res_config_settings_views.xml',
        # 'views/stock_scrap_views.xml',
        # 'views/stock_location_views.xml',

        # Wizards
        # 'wizard/stock_barcode_cancel_operation.xml',
        # 'wizard/stock_backorder_confirmation_views.xml',

        # Data Files
        # 'data/data.xml',
    ],
    'demo': [
        # 'data/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'AGPL-3',
    'assets': {
        'web.assets_backend': [
            'web/static/src/core/**/*',
            'qr_code_scanner/static/src/**/*.js',
            # 'qr_code_scanner/static/src/**/*.scss',
            'qr_code_scanner/static/src/**/*.xml',
        ],
    },
}
