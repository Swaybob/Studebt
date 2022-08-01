from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import School
# from . import forms
# Register your models here.
admin.site.register(School)


# @admin.register(School)
class SchoolAdmin(UserAdmin):
    # add_form = forms.SchoolAddForm
    # form = forms.SchoolUpdateForm
    list_display = ['reg_number', 'name', 'is_active', 'date_joined']
    # readonly_fields = ['date_joined', 'reg_number']
    search_fields = ['name']
    ordering = ['name']
    