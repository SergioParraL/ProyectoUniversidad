from django.contrib import admin
from .models import DocsDB, NotasDB

# Register your models here.

class DocsDBAdmin(admin.ModelAdmin):
    readonly_Fields=('created', 'updated')
    
class NotasDBAdmin(admin.ModelAdmin):
    readonly_Fields=('created', 'updated')


admin.site.register(DocsDB, DocsDBAdmin)
admin.site.register(NotasDB, NotasDBAdmin)