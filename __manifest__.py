# -*- coding: utf-8 -*-
{
    'name': "hr_extend",

    'summary': """
        """,

    'description': """
        It added some 
    """,

    'author': "Arash Homayounfar",
    'website': "https://github.com/gilaneh/hr_extend",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Service Desk/Service Desk',
    'application': True,
    'version': '17.0.0.2.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web','hr', 'hr_skills' ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hr_employee_views.xml',
    ],

    'license': 'LGPL-3',

}
