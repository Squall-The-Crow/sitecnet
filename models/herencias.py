# -*- coding: utf-8 -*-

from odoo import fields, models, api

class resPartner(models.Model):
    _inherit = "res.partner"
    _description = "Campos extra de clientes"

    tecnico = fields.Many2one('res.users', string='Tecnico')
    software = fields.One2many('sitecnet.complemento_software', 'cliente', string='Software')
    usuarios = fields.One2many('sitecnet.complemento_usuarios', 'cliente', string='Software')
    equipos = fields.One2many('sitecnet.complemento_equipos', 'cliente', string='Equipos')
    carpetas = fields.One2many('sitecnet.carpetas', 'cliente', string='Carpetas')
    checklist = fields.One2many('sitecnet.checklist_template', 'cliente', string='Checklist')