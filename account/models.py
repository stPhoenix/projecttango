from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class Account(AbstractUser):
    avatar = models.ImageField(default='users_avatars/avatar.jpg', upload_to='users_avatars/')

