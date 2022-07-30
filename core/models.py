from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import SchoolManager
from .utils import random_reg_num
# Create your models here.


# The core app is where we are going to be handling authentication


# The Abstract User class allows the school to leverage on django's auth system
# and still modify certain fields of choice
# Take note of line 126 of the settings.py file


class School (AbstractUser):

    username = models.CharField(
        max_length=50, unique=True, blank=True, default='Anonymous')
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=250, blank=True,
                            verbose_name='School Name')
    picture = models.ImageField(upload_to='img', blank=True)

    reg_number = models.CharField(
        editable=False, verbose_name='Registration Number', unique=True, max_length=20)

    password = models.CharField(max_length=20)

    school_category = models.ForeignKey(
        'Cat', on_delete=models.SET_NULL, unique=False, null=True)
    state = models.CharField(max_length=50, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    address = models.TextField(null=False, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = SchoolManager()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.reg_number = random_reg_num()
        super().save(*args, **kwargs)

    # The username should be the school reg. no.
    pass


# This is the profile for each school (logo, location, dates)
class Profile (models.Model):
    # logo = models.ImageField(upload_to='img', blank=True)

    pass


class Cat(models.Model):
    name = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name
