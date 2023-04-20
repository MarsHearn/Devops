from django.db import models
#from django.contrib.auth.models import User # create users
#from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class test_model(models.Model):
    t1 = models.CharField(max_length=128)
    t2 = models.CharField(max_length=128)

