from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _description = "Hospital Appointment"
    _inherit = ["mail.thread"]
    _rec_name = "patient_id"

    reference = fields.Char(string="Reference", default="New")
    patient_id = fields.Many2one("hospital.patient", string="Patient")
    date_appointment = fields.Date(string="Date")
    note = fields.Text(string="Note")
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("confirmed", "Confirmed"),
            ("ongoing", "Ongoing"),
            ("done", "Done"),
            ("cancel", "Cancel"),
        ],
        default="draft",
        tracking=True
    )

    @api.model_create_multi
    def create(self, vals):
        for val in vals:
            if val.get("reference", "New") == "New":
                    val["reference"] = self.env["ir.sequence"].next_by_code("hospital.appointment")

        return super().create(vals)
    
    def action_confirm(self):
        for rec in self:
            rec.state = "confirmed"
    
    def action_ongoing(self):
        for rec in self:
            rec.state = "ongoing"
    
    def action_done(self):
        for rec in self:
            rec.state = "done"
    
    def action_cancel(self):
        for rec in self:
            rec.state = "cancel"