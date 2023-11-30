# -*- coding: utf-8 -*-
{
    'name': "sitecnet",

    'summary': """
       Creación de procesos de negocio SITECNET""",

    'description': """
        Lista de modulos:
        Checklist
        Integración de Factura
    """,

    'author': "Sitecnet",
    'website': "https://sitecnet.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Support',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/sitecnet_security.xml',
        'security/ir.model.access.csv',        
        'views/checklist.xml',
        'views/complemento.xml',
        'views/herencias.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
