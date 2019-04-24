from django.db import models


class UserModel(models.Model):
    u_name = models.CharField(max_length=16, unique=True)
    u_age = models.IntegerField(default=1)
    u_password = models.CharField(max_length=32)
    u_token = models.CharField(max_length=32,null=True,default='')

