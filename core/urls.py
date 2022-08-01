from . import views
from django.urls import path

urlpatterns = [
    path('signup/', views.SchoolSignUpView.as_view(), name='signup'),
    # path('login/', views.SchoolLogin, name='login'),

]
