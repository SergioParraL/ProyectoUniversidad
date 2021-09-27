from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

#BBDD----------------
from .models import *

# Register your models here.

class UserAdminSystem (UserAdmin):
    fieldsets = ()
    add_fieldsets = (

        (None, {
           'fields': ('username', 'password1', 'password2', 'email', 'is_PA', 'is_PD'),
        }),
    )

    list_display = ('username', 'email', 'is_staff', 'is_PA','is_PD')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'is_PA', 'is_PD')
    ordering = ('username',)


    
class PA_profileAdmin(admin.ModelAdmin):
    readonly_Fields=('created', 'updated')

class PD_profileAdmin(admin.ModelAdmin):
    readonly_Fields=('created', 'updated')


admin.site.register(SystemUser,UserAdminSystem)
admin.site.register(PA_profile, PA_profileAdmin)
admin.site.register(PD_profile, PD_profileAdmin)