from odoo import  api, fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Patient master"

    name = fields.Char(string="Name")
    date_of_birth =fields.Date(string="DOB")
    gender = fields.Selection([("male", "Male"), ("female", "Female")])
    phone = fields.Integer(string="Phone Number")