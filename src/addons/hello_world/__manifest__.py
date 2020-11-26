# -*- coding: utf-8 -*-
{
    'name': "Hello World",

    'summary': """
        This is a very simple module, existing to demonstrate various
        development and testing practices.""",

    'description': """
        This is a very simple module, existing to demonstrate various
        development and testing practices.
    """,

    'author': "Ken LeFebvre",
    'website': "https://linkedin.com/in/kenlefeb",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customizations',
    'version': '0.3',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
