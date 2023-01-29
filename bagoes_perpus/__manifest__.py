# -*- coding: utf-8 -*-
{
    'name': "Training 29 - Perpustakaan",

    'summary': """
        Trainig 29
        by Bagoes""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Bagoes",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Training',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/book.xml',
        'views/transaction.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}
