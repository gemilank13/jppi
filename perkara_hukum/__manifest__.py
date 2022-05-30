# -*- coding: utf-8 -*-
{
    'name': "JPPI - Perkara Hukum",

    'summary': """ Modul Perkara Hukum """,
    'description': """ Modul Perkara Hukum """,
    'author': "PT JPPI - Geger Gemilank",
    'website': "http://www.jppi.co.id",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base','portal', 'mail'],

    'data': [
         'security/security.xml',
         'security/ir.model.access.csv',
         'views/config.xml',
         'views/sequence.xml',
         'views/perkara_hukum.xml',

    ],
    
    'demo': [],
}