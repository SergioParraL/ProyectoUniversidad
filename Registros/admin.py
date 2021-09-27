from django.contrib import admin
from .models import PersonalAdm, PersonalDocente, Representantes, Estudiantes

# Register your models here.

class PersonalAdmAdmin(admin.ModelAdmin):
    readonly_Fields=('created', 'updated')

class PersonalDocenteAdmin(admin.ModelAdmin):
    readonly_Fields=('created', 'updated')

class RepresentantesAdmin(admin.ModelAdmin):
    readonly_Fields=('created', 'updated')

class EstudiantesAdmin(admin.ModelAdmin):
    readonly_Fields=('created', 'updated')


admin.site.register(PersonalAdm, PersonalAdmAdmin)
admin.site.register(PersonalDocente, PersonalDocenteAdmin)
admin.site.register(Representantes, RepresentantesAdmin)
admin.site.register(Estudiantes, EstudiantesAdmin)