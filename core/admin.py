from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import School, Cat
from . import forms
# Register your models here.
admin.site.register(Cat)


@admin.register(School)
class SchoolAdmin(UserAdmin):
    add_form = forms.SchoolAddForm
    form = forms.SchoolUpdateForm
    list_display = ['reg_number', 'name', 'is_active', 'date_joined']
    readonly_fields = ['date_joined', 'reg_number']
    search_fields = ['name']
    ordering = ['name']
    fieldsets = (
        (
            'Profile', {
                'fields': ('picture', 'reg_number', 'name')
            }
        ),
        (
            None, {
                'fields': ('email', 'username')
            }
        ),
        (
            'Additional Info', {
                'fields': ('school_category', 'address', 'state')
            }
        )
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'username', 'password', 'picture', 'address', 'school_category', 'state')
        }),
    )
