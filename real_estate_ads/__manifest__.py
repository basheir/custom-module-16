{
    "name": "Real estate ads",
    "description": "This is real estate ads module for development",
    "category": "sales",
    "author": "Bashir Mahad",
    "website": "course.haybis.com",
    'installable': True,
    "application":True,
    "auto-install":True,
    "license": "LGPL-3",
    "depends": ["base"],
    'data': [
        "security/ir.model.access.csv",
        "views/property_view.xml",
        "views/property_type_view.xml",
        "views/property_tag_view.xml",
        "views/menu_views.xml",

    ],

}