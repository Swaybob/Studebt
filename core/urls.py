from . import views
from django.urls import path

urlpatterns = [
    path('signup/', views.SchoolSignup, name='signup'),
    path('login/', views.SchoolLogin, name='login'),

]
