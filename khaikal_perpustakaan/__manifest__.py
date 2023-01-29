# -*- coding: utf-8 -*-
{
    'name': "Perpustakaan",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/book.xml',
        'views/transaction.xml',
        'views/templates.xml',
        'views/sale.xml',
        'views/generate_book.xml',
        'views/inherit_report.xml',
        'data/sequence.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
