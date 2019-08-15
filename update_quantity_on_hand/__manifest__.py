{
    'name': 'Update Product Quantity on Hand Security',
    'version': '10.0',
    'author': 'Muhammad Faisal',
    'sequence': 1,
    'category': 'Warehouse',
    'website': 'http://Khatah.com',
    'summary' : 'Product on hand security',
    'description': '''
     This module will add a new security feature for the update product quantity on hand button in inventory module
    ''',
    'depends': ['stock','product'],
    'data': ['product_view_ext.xml','security/product_security_ext.xml'],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    "images":['static/description/banner.png'],

}
