from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views.generic import CreateView

from .forms import SchoolSignUpForm
from .models import CustomUser

class SchoolSignUpView(CreateView):
    model = CustomUser
    form_class = SchoolSignUpForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'school'
        return super().get_context_data(**kwargs)

    def form_valid(self,form):
        user = form.save()
        pass
