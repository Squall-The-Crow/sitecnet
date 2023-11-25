# -*- coding: utf-8 -*-

from odoo import models, fields, api

class checklist_template(models.Model):
    _name = 'sitecnet.checklist_template'
    _rec_name = 'name'
    _description = "Checklist de atención"

########Campos De sistema##############
    name = fields.Char(string='Nombre de Checklist', required=True)
    cliente = fields.Many2one('res.partner', 'Cliente')
    programacion = fields.Selection([
        ("Semanal","Semanal"),
        ("Mensual","Mensual"),
        ("Trimestral","Trimestral"),
        ("Semestral","Semestral"),
        ("Anual","Anual")],
         'Programacion')
    campos = fields.One2many('sitecnet.checklist_fields', 'name', 'Campos')

    

class checklist_fields(models.Model):
    _name = 'sitecnet.checklist_fields'
    _rec_name = 'name'
    _description = "Campos de checklist"

    name = fields.Char(string='Actividad', required=True)
    realizado = fields.Boolean('Status')
    comentario = fields.Char(string='Actividad')# tal vez poner if realizado = false

class checklist(models.Model):
    _name = 'sitecnet.checklist'
    _rec_name = 'name'
    _description = "Checklist de atención"

########Campos De sistema##############
    name = fields.Char(string='Nombre de Checklist', required=True)
    cliente = fields.Many2one('res.partner', 'Cliente')
    programacion = fields.Selection([
        ("Semanal","Semanal"),
        ("Mensual","Mensual"),
        ("Trimestral","Trimestral"),
        ("Semestral","Semestral"),
        ("Anual","Anual")],
         'Programacion')
    fecha = fields.Date('Fecha de creación')
    campos = fields.One2many('sitecnet.checklist_fields', 'name', 'Campos')
