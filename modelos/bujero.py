# -*- coding: utf-8 -*-

from odoo import models, fields, api
from . import base

class Bujero(models.Model):
    _name = 'mipollita.bujero'
    _description = 'Tipos de bujeros'
    _inherit = 'mipollita.base'
    
    name = fields.Char(string='Nombre bujero', required=True)
    genero = fields.Char(string='Genero', required=True)
    duracion = fields.Float(string='Duracion', required=True)
    radio = fields.Float(string='Radio', required=True)
    profundidad = fields.Float(string='profundidad', required=True)
    description = fields.Text(string='Resumen', required=True)

    # actor_ids = fields.Many2many('teatro.actor', string='Actores')
    # director_ids = fields.Many2one('teatro.director', string='Directores')
    # opinion_ids = fields.One2many('teatro.opinion', 'obra_id', string='Opiniones')
    # sala_id = fields.Many2one('teatro.sala', string='Sala en la que se representa la obra')
    # promocion_ids = fields.Many2many('teatro.promocion', string='Promociones')
