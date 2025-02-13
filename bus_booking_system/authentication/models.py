from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    ROLES = (('passenger', 'Passenger'), ('admin', 'Administrator'))

    role = models.CharField(max_length=15, choices=ROLES, default='passenger')
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
