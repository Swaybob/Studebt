from django.db import models
from django.conf import settings    
from django.contrib.auth import get_user_model
import datetime as dt

from core.models import School
from .utils import random_reg_num
# Take note of line 126 of the settings.py file



# Create your models here.

# my_debtors app is where we will be handling all the process and logic of our application




class Student (models.Model):

    GENDER_CHOICES = (
        (1, 'Male'),
        (2, 'Female')
    )
    CLASS_CHOICE= (
        ('Nursery 1', 'Nur 1'),
        ('Nursery 2', 'Nur 2'),
        ('Primary 1', 'Pri 1'),
        ('Primary 2', 'Pri 2'),
        ('Primary 3', 'Pri 3'),
        ('Primary 4', 'Pri 4'),
        ('Primary 5', 'Pri 5'),
        ('Primary 6', 'Pri 6'),
    )
    picture = models.ImageField(upload_to='img', null=True)
    first_name = models.CharField(max_length=30, blank=False, verbose_name='First Name', default='damnoit')
    last_name = models.CharField(max_length=30, blank=False, verbose_name='Last Name', default='damnoit')
    middle_name = models.CharField(max_length=30, verbose_name='Middle Name', null=True)
    NIN = models.BigIntegerField(null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=False, default='damnoit')
    class_name = models.CharField(max_length=20, choices=CLASS_CHOICE, blank=False, default='damnoit')

    sponsor_name = models.CharField(max_length=100, blank=False, default='Parents', verbose_name='Name of Sponsor')
    sponsor_phone = models.CharField(max_length=11, blank=False, verbose_name='Sponsor\'s Phone Number',default='damnoit')
    nationality = models.CharField(max_length=20, default='Nigerian', blank=False)

    session = models.CharField(max_length=9, null=True)

    # reg_number 
    # first_name 
    # last_name 
    # middle_name
    # email = 
    # gender = 
    # student_class 
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)


    def save(self, *args, **kwargs):
        self.reg_number = random_reg_num()
        super().save(*args, **kwargs)
    


class Profile(models.Model):
    # passport
    passport = models.ImageField(upload_to='img', null=True)
    student = models.OneToOneField(Student, on_delete=models.CASCADE, null=True)

    pass


class Debt (models.Model):
    CREDIT_STATUS = (
        ('Paid', 'paid'),
        ('owing', 'owing')
    )
    amount = models.CharField(max_length=20, null=True)
    description = models.TextField(null=True)
    credit_status = models.CharField(max_length=10, choices=CREDIT_STATUS, null=True)

    student = models.ForeignKey(Student, models.PROTECT, related_name='debt')


    

class Post (models.Model):

    title	= models.CharField(max_length=200, null=True)
    content = models.TextField(null=True)
    date_posted = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    school = models.OneToOneField(School, on_delete=models.CASCADE, null=False)
    



class Complaint (models.Model):

    # post (FOREIGN KEY)
    # student 
    # description
    # proof (if there is any- pic or pdf)

    pass

    

