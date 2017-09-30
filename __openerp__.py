{
    'name': "Zynthian Sale Order Reports",
    'version': '1.0',
    'category' : 'Website',
    'website' : 'http://www.zynthian.org',
    'summary': 'Sale Order Reports',
    'description': """
    - zynthian_report_saleorder_document --> sale.report_saleorder_document
        -- Only shipping address is show
        -- Delete Taxes fields
        -- Included payment method and their instructions
    -zynthian_website_confirmation --> website_sale.confirmation
        -- Only Shipping Address is shown and it's move from its original place
        -- Delete Taxes Field

    - IMPORTANT:
        Desactive view report_shop_saleorder_document
        """,
    'author': 'mumaker',
    'depends': [],
    'data': [
        'views/zynthian_report_saleorder_document.xml',
        'views/zynthian_website_confirmation.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}