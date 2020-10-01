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
    - zynthian_website_confirmation --> website_sale.confirmation
        -- Only Shipping Address is shown and it's move from its original place
        -- Delete Taxes Field --> Active at 1/10/20
        -- Delete product description
    - zynthain_sale_order_mail.xml
        -- New template for sale order
    - zynthian_tracker_sale_order_mail
        -- New template for tracking code mail
    - zynthian_notification_mail
        -- Copy Template "Zynthian Notification Mail" Setting->Technical->Email->Templates to "Notification Email"

    - IMPORTANT:
        Desactive view report_shop_saleorder_document
        """,
    'author': 'mumaker',
    'depends': ['mail','report','website_sale'],
    'data': [
        'views/zynthian_report_saleorder_document.xml',
        'views/zynthian_website_confirmation.xml',
        'views/zynthian_sale_order_mail.xml',
        'views/zynthian_tracker_sale_order_mail.xml',
        'views/zynthian_report_layout_header.xml',
        'views/zynthian_notification_mail.xml'
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}