# -*- coding: utf-8 -*-
{
    'name': "Bagoes Academy",

    'summary': """
        Addons training batch 29""",

    'description': """
        Addons training batch 29"
    """,

    'author': "Bagoes",
    'website': "http://www.bagoesardianjar.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/course_data.xml',
        'views/course.xml',
        'views/session.xml',
        'views/user.xml',
        'views/partner.xml',
        'wizards/wizard_attendees.xml',
        'report/session_report.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
