# -*- coding: utf-8 -*-

from odoo import models, fields

class StockPicking(models.Model):
    _name = "stock.picking"
    _inherit = 'stock.picking'

    x_courier_company = fields.Char(string='Compañía de Envío', required=False, default='', help='Este campo es para definir la compañía de envío')
