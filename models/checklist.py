# -*- coding: utf-8 -*-

from odoo import models, fields, api

class checklist(models.Model):
    _name = 'sitecnet.checklist'
    _rec_name = 'name'
    _description = "Checklist de atención"

########Campos De sistema##############
    name = fields.Char(string='Nombre de Checklist', required=True)
    tipo = fields.Selection([
        ("Onboarding","Onboarding"),
        ("Actividades","Actividades")],
         'Tecnologia')