

from odoo import  fields, models

class SchoolCategory(models.Model):
    _name = "school.category"
    _description =  "School Category"


    name = fields.Char(string='Name', require=True)
    description = fields.Text(string='Description', require=True)


