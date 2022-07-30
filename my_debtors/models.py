from django.db import models
from django.conf import settings    

# Take note of line 126 of the settings.py file



# Create your models here.

# my_debtors app is where we will be handling all the process and logic of our application




class Student (models.Model):

 

    # reg_number 
    # first_name 
    # last_name 
    # middle_name
    # email = 
    # gender = 
    # student_class 

    school = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    


class Profile(models.Model):
    # passport

    pass


class Debt (models.Model):

    # amount
    # description 
    # credit_status 

    student = models.ForeignKey(Student, models.PROTECT, related_name='debt')


    

class Post (models.Model):

    #  title	
    # content
    # date posted 
    # date updated
    school = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='post')
    



class Complaint (models.Model):

    # post (FOREIGN KEY)
    # student 
    # description
    # proof (if there is any- pic or pdf)

    pass

    

