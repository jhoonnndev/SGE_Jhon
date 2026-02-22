# clase WorkPlace
from odoo import models, fields

class WorkPlace(models.Model):
    _name = 'examen.workplace'
    _description = 'Lugar de Trabajo'

    name = fields.Char(string="Nombre del lugar", required=True)
    horario = fields.Char(string="Horario de apertura")

# clase SleepPlace con fecha para la vista calendario
class SleepPlace(models.Model):
    _name = 'examen.sleepplace'
    _description = 'Lugar para dormir'

    name = fields.Char(string="Nombre del lugar", required=True)
    fecha = fields.Date(string="Fecha de disponibilidad")


# necisto una clase persona con un campo varios a muchos con workplace 
class Person(models.Model):
    _name = 'examen.person'
    _description = 'Persona'

    name = fields.Char(string="Nombre de la persona", required=True)
    workplaces_id  = fields.Many2many('examen.workplace', string="Lugares de trabajo")


# clase Hospital que hereda con inherit de SleeepPlace y WorkPlace
class Hospital(models.Model):
    _name = 'examen.hospital'
    _description = 'Hospital'
    _inherit = ['examen.sleepplace', 'examen.workplace']

    urgencias = fields.Boolean(string="Tiene urgencias")
    patients_ids = fields.One2many('examen.paciente', 'hospital_id', string="Pacientes")

# clase Paciente con un campo de relacion many2one con hospital
class Paciente(models.Model):
    _name = 'examen.paciente'
    _description = 'Paciente'

    name = fields.Char(string="Nombre del paciente", required=True)
    hospital_id = fields.Many2one('examen.hospital', string="Hospital al que pertenece")

#clase Empresa que hereda de WorkPlace y tiene un campo de relacion one2Many con empleado
class Empresa(models.Model):
    _name = 'examen.empresa'
    _description = 'Empresa'
    _inherit = ['examen.workplace']

    employees_ids = fields.One2many('examen.empleado', 'empresa_id', string="Empleados")

# clase Empleado con un campo de relacion many2one con empresa
class Empleado(models.Model):
    _name = 'examen.empleado'
    _description = 'Empleado'

    name = fields.Char(string="Nombre del empleado", required=True)
    empresa_id = fields.Many2one('examen.empresa', string="Empresa a la que pertenece")


    
    


