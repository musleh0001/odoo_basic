from odoo import _, api, fields, models
from odoo.exceptions import UserError


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Patient Master"
    _inherit = ["mail.thread"]

    name = fields.Char(string="Name", required=True, tracking=True)
    date_of_birth = fields.Date(string="DOB", tracking=True)
    gender = fields.Selection(
        [
            ("male", "Male"),
            ("female", "Female"),
        ],
        string="Gender",
        tracking=True
    )
    tag_ids = fields.Many2many("patient.tag", "patient_tag_rel", "patient_id", "tag_id", string="Tags")

    @api.ondelete(at_uninstall=False)
    def _check_patient_appointment(self):
        for rec in self:
            domain = [("patient_id", "=", rec.id)]
            appointments = self.env["hospital.appointment"].search(domain)
            if appointments:
                raise UserError(_("You can't delete the patient now.\nAppointments existing for this patient: %s" % rec.name))

    def unlink(self):
        return super().unlink()