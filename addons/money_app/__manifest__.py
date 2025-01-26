{
    "name": "Money App",
    "version": "1.0",
    "category": "Accounting",
    "summary": "Manage your income and expenses with ease",
    "description": """
        Money App helps you manage your personal or business finances by allowing you to:
        - Enter add track income and expenses
        - View entries in various format (tree, form, kanban and graph)
        - Automaticall calculate your remaining balance
        - Easily differentiate between income and expense transactions 
        - Get a balance summary on-damand
    """,
    "author": "Md Musleh Uddin Khan",
    "license": "LGPL-3",
    "depends": ["base", "web", "website"],
    "data": [
        "security/ir.model.access.csv",

        "data/cron.xml",
        "data/email_template.xml",

        "views/money_entry_views.xml",
        "views/balance_template.xml"
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
    "maintainers": ["musleh"],
}
