from django.db import models


class UserModel(models.Model):
    u_name = models.CharField(max_length=16)
    u_icon = models.ImageField(upload_to='icons')