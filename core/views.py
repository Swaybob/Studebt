from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

from .models import School
from .forms import SchoolSignupForm, SchoolLoginForm

# Create your views here.


def SchoolSignup(request):
    if request.method == 'POST':
        form = SchoolSignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = School.objects.create_superuser(
                email=email, password=password)
            user.save()
            return redirect('login')
        else:
            # form = SchoolAddForm()
            # context = {'form': form}
            # return render(request, 'signup.html', context)
            return HttpResponse('Problem!')
    else:
        # form = SchoolAddForm()
        # context = {'form': form}
        # return render(request, 'signup.html', context)
        return HttpResponse('Request Problem')


def SchoolLogin(request):
    if request.method == 'POST':
        form = SchoolLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(user)
            return HttpResponse('Successful')
        else:
            form = SchoolLoginForm()
            context = {'form': form}
            return render(request, 'login.html', context)
    else:
        form = SchoolLoginForm()
        context = {'form': form}
        return render(request, 'login.html', context)
