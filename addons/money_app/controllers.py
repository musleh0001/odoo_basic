from odoo import http 
from odoo.http import request

class MoneyAppController(http.Controller):
    @http.route("/money/balance", auth="public", website=True)
    def show_balance(self, **kwargs):
        entries = request.env["money.entry"].search([])
        income = sum(entry.amount for entry in entries if entry.type == "income")
        expense = sum(entry.amount for entry in entries if entry.type == "expense")
        balance = income - expense

        return request.render("money_app.balance_template", {
            "balance": balance,
            "entries": entries
        })