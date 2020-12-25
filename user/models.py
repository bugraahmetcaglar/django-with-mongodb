from django.contrib.auth.models import AbstractUser
from djongo import models


class User(AbstractUser):
    access_token = models.TextField(unique=True)

    def __str__(self):
        return self.username

    def __unicode__(self):
        return self.username

    class Meta:
        db_table = "user"
