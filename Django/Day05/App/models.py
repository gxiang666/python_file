from django.db import models


class Animal(models.Model):
    a_name = models.CharField(max_length=16)
    a_color = models.IntegerField(default=255)

    def get_age(self):
        return 180

    def __str__(self):
        return self.a_name
