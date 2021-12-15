from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    GENDER_CHOICES = {
        ('m', 'Male'),
        ('f', 'Female')
    }
    username = models.CharField(
        max_length=255,
        unique=True
    )
    image = models.ImageField(
        upload_to='images',
        blank=True,
        null=True
    )
    age = models.PositiveIntegerField(
        default=0
    )
    gender = models.CharField(
        choices=GENDER_CHOICES,
        max_length=10
    )

    def __str__(self):
        return self.username
