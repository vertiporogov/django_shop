from django.contrib.auth.models import AbstractUser
from django.db import models

from blog.models import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='email')

    phone = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', **NULLABLE, verbose_name='аватар')
    country = models.CharField(max_length=50, **NULLABLE, verbose_name='страна')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
