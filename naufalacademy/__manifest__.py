# -*- coding: utf-8 -*-
{
    'name': "Naufal Academy",

    'summary': """
        Addons training batch 29""",

    'description': """
        Addons training batch 29"
    """,

    'author': "Naufal Nabila",
    'website': "http://www.naufalnabila.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
