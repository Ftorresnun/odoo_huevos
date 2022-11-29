# -*- coding: utf-8 -*-

from odoo import models, fields, api
from . import base

class Pana(models.Model):
    _name = 'mipollita.pana'
    _description = 'Tipos de panas'
    _inherit = 'mipollita.base'
    
    name = fields.Char(string="Nombre", required=True)
    raza = fields.Char(string="Raza")
    description = fields.Text(string="Descripción")
    sexo = fields.Selection([('Hombre', 'Hombre')('Hembra', 'Hembra')], string="Sexo")
    