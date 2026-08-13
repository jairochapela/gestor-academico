from django.db import models

from auditlog.registry import auditlog

from django.views.generic import ListView


# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.nombre


auditlog.register(Curso)  # Register the Curso model with auditlog

class Empresa(models.Model):
    nombre = models.CharField(max_length=100)
    razon_social = models.CharField(max_length=400)
    direccion_practicas = models.CharField(max_length=400, null=True, blank=True)
    cif = models.CharField(max_length=10, unique=True)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    responsable = models.CharField(max_length=200)
    tutor = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

auditlog.register(Empresa)  # Register the Empresa model with auditlog


class Horario(models.Model):
    descripcion = models.TextField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    

auditlog.register(Horario)  # Register the Horario model with auditlog


class Alumno(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    apellidos = models.CharField(max_length=100, null=False, blank=False)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    nif_nie = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True, blank=True)
    horario_practicas = models.ForeignKey(Horario, on_delete=models.SET_NULL, null=True, blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"


auditlog.register(Alumno)  # Register the Alumno model with auditlog