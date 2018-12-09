from django.db import models
from .managers import UserManager
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
# Create your models here.


class Website(models.Model):
    company_name = models.CharField(max_length=200)
    business_type = models.CharField(max_length=200)
    owner_name = models.CharField(max_length=200)
    domain = models.CharField(max_length=200)
    website_type = models.CharField(max_length=200)
    def __str__(self):
        return self.domain

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    website_url = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=200)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.first_name + ' ' +  self.last_name + self.email
