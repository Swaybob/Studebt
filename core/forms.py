from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms
from . import models


class SchoolAddForm(UserCreationForm):
    class Meta:
        model = models.School
        fields = ['picture', 'name', 'username', 'email',
                  'address', 'school_category', 'state']


class SchoolUpdateForm(UserChangeForm):
    class Meta:
        model = models.School
        fields = ['picture', 'name', 'username', 'email',
                  'address', 'school_category', 'state']


class SchoolLoginForm(AuthenticationForm):
    class Meta:
        model = models.School
        fields = ['email', 'password']


class SchoolSignupForm(forms.Form):
    class Meta:
        model = models.School
        fields = ['picture', 'name', 'username', 'email',
                  'address', 'school_category', 'state']
