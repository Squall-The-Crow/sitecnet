# -*- coding: utf-8 -*-

from odoo import fields, models, api

class complemento_usuarios(models.Model):
    _name = 'sitecnet.complemento_usuarios'
    _description = "Información complementaria de usuarios"

    name = fields.Char('Nombre')
    depto = fields.Char('Departamento')
    telefono = fields.Char('Telefono')
    correo = fields.Char('Correo')
    tier = fields.Many2one('product.template', string='Tier') #Asignar filtro de solo servicios
    equipos = fields.One2many('sitecnet.complemento_equipos', 'usuario', 'Equipos')
    software = fields.One2many('sitecnet.software', 'usuario', 'Software permitido')
    cliente = fields.Many2one('res.partner', 'Cliente')
    carpetas = fields.Many2many('sitecnet.carpetas', 'carpeta_usuario_rel', 'usuario_id', 'carpeta_id', string='Carpetas Relacionadas')



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
    renovacion = fields.Char('Periodo de renovación')#Asignar filtro de solo perpetual = false
    perpetual = fields.Boolean('Perpetual')
    adquisicion = fields.Selection([
    	("Rentado","Rentado"),
    	("Comprado","Comprado"),
    	("Externo","Externo")], 
    	'Adquisicion')
    proveedor = fields.Many2one('sitecnet.proveedor', 'Proveedor Externo')
    usuario = fields.Many2one('sitecnet.complemento_usuarios', 'Usuario')

class CarpetaUsuarioRel(models.Model):
    _name = 'carpeta_usuario_rel'
    _description = "Tabla relacional de carpetas y usuarios"

    carpeta_id = fields.Many2one('sitecnet.carpetas', string='Carpeta', index=True)
    usuario_id = fields.Many2one('sitecnet.complemento_usuarios', string='Usuario', index=True)
    permisos = fields.Selection([
        ('lectura', 'Lectura'),
        ('escritura', 'Escritura'),
        ('propietario', 'Propietario')],
        string='Nivel de acceso',
        default='lectura',
        help='Tipo de relación entre Carpeta y Usuario'
    )

    _sql_constraints = [
        ('relacion_unico', 'unique(carpeta_id, usuario_id, permisos)', 'La relación debe ser única por carpeta y usuario.'),
    ]

class carpetas(models.Model):
    _name = 'sitecnet.carpetas'
    _description = "Información complementaria de permisos de carpetas"

    name = fields.Char('Nombre de la carpeta')
    ubicacion = fields.Char('Ubicación de la carpeta')
    alojado = fields.Selection([
    	("Local","Local"),
    	("Nube","Nube")], 
    	'Alojamiento')
    usuarios = fields.Many2many('sitecnet.complemento_usuarios', 'carpeta_usuario_rel', 'carpeta_id', 'usuario_id', string='Usuarios Relacionados')
    cliente = fields.Many2one('res.partner', 'Cliente')

class servicios(models.Model):
    _name = 'sitecnet.servicios'
    _description = "Información complementaria de servicios contratados"

    name = fields.Char('Nombre del servicio')
    cliente = fields.Many2one('res.partner', 'Cliente')
    terminos = fields.Text('Terminos del servicio')
    checklist = fields.One2many('sitecnet.checklist', 'name', 'Checklist asociados')