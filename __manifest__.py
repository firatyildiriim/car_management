{
    'name': 'Company Car Management',
    'author': 'Fırat Yıldırım',
    'sequence': -101,
    'application': True,
    'category': 'Car Fleet Organization',
    'version': '1.0.0',
    'depends': ['mail',
                ],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/car_view.xml',
    ],
    'demo': [],
}