# -*- coding: utf-8 -*-
{
    'name': "zz",

    'summary': """
        模块1
        """,
    'description': """
        模块2
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Bicon',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/mytest.xml',
        'views/mytest1.xml',


    ]
}
