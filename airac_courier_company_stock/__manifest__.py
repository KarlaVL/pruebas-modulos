# -*- coding: utf-8 -*-
{
    'name': "airac_courier_company_stock",

    'summary': """
        Este campo es oara Inventario y definir la compañia de envío""",

    'description': """
        Inventario 01
    """,

    'author': "Ideanet",
    'website': "http://www.ideanet.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/stock_picking_form.xml',
        'report_stockpicking.xml'
    ],
}
