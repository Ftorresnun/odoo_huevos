# -*- coding: utf-8 -*-

from odoo import models, fields, api
from . import pana

class Pollita(models.Model):
    _name = 'mipollita.pollita'
    _description = 'Tipos de pollas'
    _inherit = 'mipollita.pana'
    
    name = fields.Char(string="Nombre", required=True)
    tamanyo = fields.Integer(string="Raza")
    description = fields.Text(string="Descripción")
    peso = fields.Integer(string="Peso")
    
    # huevos_ids = fields.One2many('mipollita.huevos', 'pollita_id', string='huevos de la polla')