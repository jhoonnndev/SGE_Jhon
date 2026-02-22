{
    'name': 'Gestión de Biblioteca',
    'summary': 'me encanta odoo 19',
    'description': 'Biblioteca en Odoo 19',
    'author': 'Jhon',
    'website': "http://www.iespabloserrano.com",

    'category': 'odoo',
    'version': '0.1',

    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/autor_views.xml',
        'views/libro_views.xml',
        'views/prestamo_views.xml',
        'views/menu.xml',
    ],
}