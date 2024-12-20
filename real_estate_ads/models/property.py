from odoo import models, fields, api



class Property(models.Model):
    _name = "estate.property"
    _description = "Estate Property"

    name = fields.Char(string="Name")
    tag_ads = fields.Many2many("estate.property.tag", string="Property Tag")
    type_id = fields.Many2one("estate.property.type", string="Property Type")
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Post Code")
    date_availability = fields.Date(string="Available From")
    best_offer = fields.Float(string="Best Offer")
    expected_price = fields.Float(string="Expected Price")
    selling_price = fields.Float(string="Selling Price")
    bedrooms = fields.Integer(string="Bedrooms")
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage", default=False)
    garden = fields.Boolean(string="Garden", default=False)
    garden_area = fields.Integer(string="Garden Area")
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ], string="Garden Orientation", default='north')
    offer_ads = fields.One2many("estate.property.offer", "property_id", string="Offers")


class PropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Property type"

    name = fields.Char(string="Name", required=True)


class PropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Property Tag"

    name = fields.Char(string="Name", required=True)