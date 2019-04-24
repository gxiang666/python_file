from django.db import models


class UserModel(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=128)
    email = models.CharField(max_length=64)
    is_delete = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
