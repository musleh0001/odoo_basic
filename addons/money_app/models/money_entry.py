from odoo import models, fields, api


class MoneyEntry(models.Model):
    _name = "money.entry"
    _description = "Money Entry"

    name = fields.Char(string="Description", required=True)
    date = fields.Date(string="Date", default=fields.Date.today)
    amount = fields.Float(string="Amount", required=True)
    type = fields.Selection(
        [("income", "Income"), ("expense", "Expense")], string="Type", required=True
    )
    balance = fields.Float(compute="_compute_balance", string="Balance", readonly=True)


    @api.depends("type", "amount")
    def _compute_balance(self):
        for record in self:
            income = sum(self.search([("type", "=", "income")]).mapped("amount"))
            expenses = sum(self.search([("type", "=", "expense")]).mapped("amount"))

            record.balance = income - expenses
    
    def get_balance2(self):
        income = sum(self.search([("type", "=", "income")]).mapped("amount"))
        expenses = sum(self.search([("type", "=", "expense")]).mapped("amount"))
        balance = income - expenses

        return {
            "type": "ir.actions.client",
            "tag": "display_notification",
            "params": {
                "title": "current balance",
                "message": f"The current balance is: {balance}",
                "sticky": False
            }
        }
    
    def send_balance_email(self):
        income = sum(self.search([("type", "=", "income")]).mapped("amount"))
        expenses = sum(self.search([("type", "=", "expense")]).mapped("amount"))
        balance = income - expenses

        template = self.env.ref('money_app.money_entry_balance_email_template')

        if template:
            template.with_context(balance=balance).send_mail(self.id, force_send=True)
