from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model

from .managers import CustomUserManager
from .utils import random_reg_num
# Create your models here.


# The core app is where we are going to be handling authentication


# The Abstract User class allows the school to leverage on django's auth system
# and still modify certain fields of choice
# Take note of line 126 of the settings.py file


class CustomUser(AbstractUser):

    username = None #models.CharField(max_length=50, unique=True, blank=True, default='Anonymous')
    email = models.EmailField(unique=True)
    # name = models.CharField(max_length=250, blank=True,
    #                         verbose_name='School Name')
    

    reg_number = models.CharField(
        editable=False, verbose_name='Registration Number', unique=True, max_length=20)

    password = models.CharField(max_length=20)
    is_student = models.BooleanField()
    is_school = models.BooleanField()
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    address = models.TextField(null=False, blank=True)

    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()



    # The username should be the school reg. no.
    pass


# This is the profile for each school (logo, location, dates)
class School (models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, null=True)
    logo = models.ImageField(upload_to='img', blank=True, null=True)
    name = models.CharField(max_length=100, blank=False,verbose_name='School Name', default='School Name')
    local_gov = models.CharField(max_length=100, blank=True, default='Alimosho')
    school_category = models.CharField(max_length=20, null=True)
    

    
    def save(self, *args, **kwargs):
        self.reg_number = random_reg_num()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    pass
