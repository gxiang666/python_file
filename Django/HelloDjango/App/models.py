from django.db import models


# model 是和数据库对应的，django中只支持关系型数据库
# 表名 字段名
class Person(models.Model):
    p_name = models.CharField(max_length=16)
    p_age = models.IntegerField(default=1)


# 拒绝中文，空格，特殊字符，数字开头...
# 拒绝关键字和保留字
class Grade(models.Model):
    g_name = models.CharField(max_length=32)


class Student(models.Model):
    s_name = models.CharField(max_length=16)
    s_age = models.IntegerField(default=1)
    s_grade = models.ForeignKey(Grade)