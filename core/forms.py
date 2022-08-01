from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import School, CustomUser

class SchoolSignUpForm(UserCreationForm):
    # user = forms.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    logo = forms.ImageField()
    name = forms.CharField(max_length=100)
    local_gov = forms.CharField(max_length=100)
    school_category = forms.CharField(max_length=20)

    class Meta:
        model = CustomUser
        fields = ['email','password','address','logo', 'name', 'local_gov', 'school_category']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_school =True
        user.is_admin = True
        user.save()
        school = School.objects.create(user=user)
        school.logo.add(*self.cleaned_data.get('logo'))
        school.name.add(*self.cleaned_data.get('name'))
        school.local_gov.add(*self.cleaned_data.get('local_gov'))
        school.school_category.add(*self.cleaned_data.get('school_category'))
        return user
