from odoo import  api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread"]
    _description = "Patient master"

    name = fields.Char(string="Name", required=True, tracking=True)
    date_of_birth =fields.Date(string="DOB", tracking=True)
    gender = fields.Selection([("male", "Male"), ("female", "Female")], tracking=True)
    phone = fields.Integer(string="Phone Number", tracking=True)