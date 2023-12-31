# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta
import logging
_logger = logging.getLogger(__name__)

class Checklist(models.Model):
    _name = 'sitecnet.checklist'
    _rec_name = 'name'
    _description = "Checklist de atención"

    name = fields.Char(string='Nombre de Checklist', required=True)
    cliente = fields.Many2one('res.partner', 'Cliente')
    frequency = fields.Selection(
        [('daily', 'Diario'),
         ('weekly', 'Semanal'),
         ('monthly', 'Mensual'),
         ('quarterly', 'Trimestral'),
         ('semiannual', 'Semestral'),
         ('annual', 'Anual')],
        string='Frequency',
        required=True,
    )
    recurrence_interval = fields.Integer(
        string='Recurrence Interval',
        default=1,
        help='Number of units between recurrences',
    )
    tareas = fields.One2many('sitecnet.tareas', 'checklist', 'Tareas')
    tareas_template = fields.One2many('sitecnet.tareas_template', 'checklist', 'Plantilla de tareas')
    inicio = fields.Date('inicio de las tareas')

    def generate_recurring_tasks(self):
        for task_list in self:
            start_date = task_list.inicio
            end_date = task_list.inicio + relativedelta(years=1)

            if task_list.frequency == 'daily':
                interval_type = 'days'
            elif task_list.frequency == 'weekly':
                interval_type = 'weeks'
            elif task_list.frequency == 'monthly':
                interval_type = 'months'
            elif task_list.frequency == 'quarterly':
                interval_type = 'months'
            elif task_list.frequency == 'semiannual':
                interval_type = 'months'
            elif task_list.frequency == 'annual':
                interval_type = 'years'
            else:
                continue

            while start_date < end_date:
                _logger.info(f"Start Date: {start_date}")
                for task in task_list.tareas_template:
                    print("Start Date:", start_date)
                    _logger.info(f"Start Date: {start_date}")
                    task_date = start_date + relativedelta(**{interval_type: task_list.recurrence_interval})
                    print("Task Date:", task_date) 
                    year, week, _ = task_date.isocalendar()
                    # si ya se genero una tarea no volver a duplicarla y solo crear las tareas que no existan
                    if not self.env['sitecnet.tareas'].search([('name', '=', f"{task.name} - {week}"),('cliente', '=', task.cliente.id)]):
                  
                        self.env['sitecnet.tareas'].create({
                            'name': f"{task.name} - {week}",
                            'checklist': task_list.id,
                            'fecha': task_date,
                            'cliente': task.cliente.id,
                            'periodo': f"{year} - {week}",
                        })

                # Incrementa la fecha de inicio al final de cada iteración del bucle exterior
                start_date += relativedelta(**{interval_type: task_list.recurrence_interval})
                

class tareas(models.Model):
    _name = 'sitecnet.tareas'
    _rec_name = 'name'
    _description = "Campos de checklist"
    name = fields.Char(string='Actividad', required=True)
    status = fields.Selection([
        ("programada","Programada"),
        ("pendiente","Pendiente"),
        ("caducada","Caducada"),
        ("realizada","Realizada"),
        ("error","Error")],
         'Estado', default='programada')
    feedback = fields.Char(string='información')
    fecha = fields.Date('Fecha de la tarea')
    checklist = fields.Many2one('sitecnet.checklist', 'checklist asociado')
    periodo = fields.Char('periodo')
    cliente = fields.Many2one('res.partner', 'Cliente')

class tareas_template(models.Model):
    _name = 'sitecnet.tareas_template'
    _rec_name = 'name'
    _description = "Campos de checklist"
    name = fields.Char(string='Actividad', required=True)
    status = fields.Selection([
        ("programada","Programada"),
        ("pendiente","Pendiente"),
        ("caducada","Caducada"),
        ("realizada","Realizada"),
        ("error","Error")],
         'Estado', default='programada')
    feedback = fields.Char(string='información')
    fecha = fields.Date('Fecha de la tarea')
    checklist = fields.Many2one('sitecnet.checklist', 'checklist asociado')
    periodo = fields.Char('periodo')
    cliente = fields.Many2one('res.partner', 'Cliente')


    def mark_completed(self):
        self.state = 'Realizada'

    def send_ticket(self):
        self.ensure_one()

        # Crear el contenido del correo
        subject = f"error en la tarea: {self.name}"
        body = f"La tarea '{self.name}' está marcada como {self.state}.\nDescripción: {self.feedback}"

        # Enviar el correo
        mail_values = {
            'subject': subject,
            'body_html': body,
            'email_from': 'soporte@sitecnet.com',
            'email_to': 'soporte@sitecnet.com',
        }
        self.env['mail.mail'].create(mail_values).send()

        return True
