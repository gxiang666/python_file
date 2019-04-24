from django.db import models


class Buyer(models.Model):
    b_name = models.CharField(max_length=32)
    b_level = models.IntegerField(default=1)


class Goods(models.Model):
    g_name = models.CharField(max_length=128)
    g_price = models.FloatField(default=1)
    g_buyers = models.ManyToManyField(Buyer)


class Animal(models.Model):
    a_name = models.CharField(max_length=16, default='Animal')
    a_legs = models.IntegerField(default=4)

    class Meta:
        abstract = True


class Dog(Animal):
    d_fun = models.TextField()


class Cat(Animal):
    c_fun = models.TextField()
