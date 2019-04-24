from django.db import models
from tinymce.models import HTMLField


class Grade(models.Model):
    g_name = models.CharField(max_length=16)
    g_type = models.IntegerField(default=1)
    g_student_count = models.IntegerField(default=30)
    g_position = models.CharField(default='1教室', max_length=32)

    def __str__(self):
        return self.g_name


class Student(models.Model):
    s_name = models.CharField(max_length=16)
    s_age = models.IntegerField(default=18)
    # 性别 False 为 女
    s_sex = models.BooleanField(default=False)

    s_grade = models.ForeignKey(Grade,default=None, null=True)

    def __str__(self):
        return self.s_name


class Blog(models.Model):
    b_content = HTMLField()
    b_author = models.CharField(max_length=32)