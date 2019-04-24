from django.db import models


class Grade(models.Model):
    g_name = models.CharField(max_length=16)


class Student(models.Model):
    s_name = models.CharField(max_length=16)
    s_age = models.IntegerField(default=1)
    s_grade = models.ForeignKey(Grade)
