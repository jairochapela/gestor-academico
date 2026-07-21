from django.contrib import admin
from practicas.models import Curso, Empresa, Horario, Alumno

# Register your models here.
admin.site.register(Curso)

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'razon_social', 'cif')
    search_fields = ('nombre', 'razon_social', 'cif', 'email', 'responsable', 'tutor')

admin.site.register(Empresa, EmpresaAdmin)


admin.site.register(Horario)

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'nif_nie', 'email')
    search_fields = ('nombre', 'apellidos', 'nif_nie', 'email')
    list_filter = ('curso', 'empresa')

admin.site.register(Alumno, AlumnoAdmin)