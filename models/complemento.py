# -*- coding: utf-8 -*-

from odoo import fields, models, api

class complemento_usuarios(models.Model):
    _name = 'sitecnet.complemento_usuarios'
    _description = "Información complementaria de usuarios"

    name = fields.Char('Nombre')
    depto = fields.Char('Departamento')
    telefono = fields.Char('Telefono')
    telefono2 = fields.Char('Telefono Secundario')
    correo = fields.Char('Correo')
    tier = fields.Many2one('product.product', string='Tier')
    equipos = fields.One2many('sitecnet.complemento_equipos', 'usuario', 'Equipos')
    software = fields.One2many('sitecnet.software', 'usuario', 'Software permitido')
    cliente = fields.Many2one('res.partner', 'Cliente')
    carpetas = fields.Many2one('sitecnet.carpetas', string='Carpetas Relacionadas')
    carpetas_relacion = fields.One2many('sitecnet.usuario_carpeta_relacion', 'usuario_id', 'Carpetas Relacionadas')

class UsuarioCarpetaRelacion(models.Model):
    _name = 'sitecnet.usuario_carpeta_relacion'
    _description = "Relación entre usuarios y carpetas"

    usuario_id = fields.Many2one('sitecnet.complemento_usuarios', 'Usuario')
    carpeta_id = fields.Many2one('sitecnet.carpetas', 'Carpeta')
    tipo_relacion = fields.Selection([
    	("lectura","Lectura"),
    	("escritura","Escritura"),
    	("administrador","Administrador"),
        ("bloqueado","Bloqueado")], 
    	'Acceso')


class complemento_equipos(models.Model):
    _name = 'sitecnet.complemento_equipos'
    _description = "Información complementaria de equipos"
    name = fields.Char('Nombre interno') # Nombre dado por el personal
    fecha_compra = fields.Date('Fecha de compra')
    factura = fields.Char('Numero de factura de compra')
    tipo = fields.Selection([
    	("PC","PC"),
    	("Lap","Lap"),
    	("Cel","Cel")], 
    	'Tipo de Equipo')
    adquisicion = fields.Selection([
    	("Rentado","Rentado"),
    	("Comprado","Comprado"),
    	("Externo","Externo")], 
    	'Adquisicion')
    proveedor = fields.Many2one('sitecnet.proveedor', 'Proveedor Externo') #filtrar por adquisición externa
    garantia = fields.Date('Fin de garantia')
    arrendamiento = fields.Many2one('sitecnet.arrendamiento') #filtrar por adquisición rentado
    nombre = fields.Char('Nombre del dispositivo')
    usuario = fields.Many2one('sitecnet.complemento_usuarios', 'Usuario')
    cliente = fields.Many2one('res.partner', 'Cliente') #related="usuario.cliente.id", store=True)
    agente_inventario = fields.Boolean('AG Inventario')
    agente_soporte = fields.Boolean('AG Soporte')
    agente_seguridad = fields.Boolean('AG Seguridad')
    agente_seguridad_red = fields.Boolean('AG Seguridad Red')
    agente_seguridad_dlp = fields.Boolean('AG Seguridad DLP')
    agente_remoto_alternativo = fields.Boolean('AG remoto alt')
    autenticacion = fields.Char('metodo de autenticacion')
    registrado = fields.Boolean('Registrado en forma de autenticacion')
    software = fields.Many2many('sitecnet.software', string='Software instalado')



class complemento_proveedor(models.Model):
    _name = 'sitecnet.proveedor'
    _description = "Información complementaria para proveedores externos"

    name = fields.Char('Nombre')
    direccion = fields.Char('Dirección')
    correo = fields.Char('Correo')
    telefono = fields.Char('Telefono')
    telefono2 = fields.Char('Telefono Secundario')
    horario = fields.Char('Horario de atención')
    notas = fields.Text('Notas')

class arrendamiento(models.Model):
    _name = 'sitecnet.arrendamiento'
    _description = "Información complementaria para equipos arrendados"

    name = fields.Char('Contrato')
    equipos = fields.One2many('sitecnet.complemento_equipos', 'arrendamiento', 'Equipos arrendados')
    tiempo = fields.Char('Tiempo de contratacion')
    inicio = fields.Date('inicio de arrendamiento')
    fin = fields.Date('Fin de arrendamiento')
    cliente = fields.Many2one('res.partner', 'Cliente')
    #complemento para archivo de contrato

class software(models.Model):
    _name = 'sitecnet.software'
    _description = "Información complementaria de softwar"

    name = fields.Char('Nombre')
    licencia = fields.Char('Licencia')
    cliente = fields.Many2one('res.partner', 'Cliente')
    renovacion = fields.Char('Periodo de renovación')#Asignar filtro de solo perpetual = false y calendarizar renovacion
    equipos = fields.Many2many('sitecnet.complemento_equipos', string='Equipos instalados')
    perpetual = fields.Boolean('Perpetual')
    adquisicion = fields.Selection([
    	("Rentado","Rentado"),
    	("Comprado","Comprado"),
    	("Externo","Externo")], 
    	'Adquisicion')
    proveedor = fields.Many2one('sitecnet.proveedor', 'Proveedor Externo')
    usuario = fields.Many2one('sitecnet.complemento_usuarios', 'Usuario')


class carpetas(models.Model):
    _name = 'sitecnet.carpetas'
    _description = "Información complementaria de permisos de carpetas"

    name = fields.Char('Nombre de la carpeta')
    ubicacion = fields.Char('Ubicación de la carpeta')
    alojado = fields.Selection([
    	("Local","Local"),
    	("Nube","Nube")], 
    	'Alojamiento')
    usuarios = fields.Many2one('sitecnet.complemento_usuarios',  string='Usuarios Relacionados')
    cliente = fields.Many2one('res.partner', 'Cliente')
    usuarios_relacion = fields.One2many('sitecnet.usuario_carpeta_relacion', 'carpeta_id', 'Usuarios Relacionados')

class servicios(models.Model):
    _name = 'sitecnet.servicios'
    _description = "Información complementaria de servicios contratados"

    name = fields.Char('Nombre del servicio')
    cliente = fields.Many2one('res.partner', 'Cliente')
    terminos = fields.Text('Terminos del servicio')
    checklist = fields.One2many('sitecnet.checklist', 'name', 'Checklist asociados')