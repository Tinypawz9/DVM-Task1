from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    roles = (('passenger', 'Passenger'), ('admin', 'Administrator'))

    role = models.CharField(max_length=15, choices=roles, default='passenger')
