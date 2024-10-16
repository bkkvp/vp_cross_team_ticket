# -*- coding: utf-8 -*-
{
    'name': 'VP ',
    'version': '17.0.1.0',
    'category': 'Tools',
    'summary': 'BKK VerbundPlus ',
    'description': """
        -
    """,
    'author': 'Christian Bopp, BKK VerbundPlus',
    'license': 'LGPL-3',
    'depends': ['web'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_users_view.xml',
        'views/database_switch_view.xml',
    ],
    'installable': True,
    'application': True,
    'images': ['static/description/icon.png']
}
