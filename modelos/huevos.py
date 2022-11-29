# -*- coding: utf-8 -*-

from odoo import models, fields, api
from . import pana 

class Huevos(models.Model):
    _name = 'mipollita.huevos'
    _description = 'Tipos de huevos'
    _inherit = 'mipollita.pana'
    
    name = fields.Char(string="Nombre", required=True)
    description = fields.Text(string="Descripción")
    
    # pollita_ids = fields.Many2one('mipollita.pollita', string='polla')
    