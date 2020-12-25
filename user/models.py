import uuid

from django.contrib.auth.models import AbstractUser
from djongo import models


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    deleted = models.BooleanField(default=False)
    gsm = models.CharField(max_length=10)
    companyName = models.CharField(max_length=254)
    lon = models.FloatField()
    lat = models.FloatField()
    dbId = models.IntegerField()
    cityId = models.IntegerField()
    taxNum = models.IntegerField()
    taxAdmin = models.CharField(max_length=100)
    email = models.CharField(blank=True, null=True, unique=True, max_length=100)
    username = models.CharField(blank=False, null=False, unique=True, max_length=10)
    remote_token = models.TextField(unique=True)
    access_token = models.TextField(unique=True)

    def __str__(self):
        return self.username

    def __unicode__(self):
        return self.username

    class Meta:
        db_table = "user"
