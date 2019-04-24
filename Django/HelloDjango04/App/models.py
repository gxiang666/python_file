from django.db import models


class MyManager(models.Manager):

    def create_model(self,d_name, d_legs = 2):
        dog = self.model()
        dog.d_name = d_name
        dog.d_legs = d_legs
        return dog

    # 先调用model.Manager get_queryset
    def get_queryset(self):
        return super(MyManager,self).get_queryset().exclude(is_delete=True)


class Dog(models.Model):
    d_name = models.CharField(max_length=16)
    d_legs = models.IntegerField(default=4)
    is_delete = models.BooleanField(default=False)

    d_manager = MyManager()


class Person(models.Model):
    p_name = models.CharField(max_length=16)
    p_age = models.IntegerField(default=1)


class IDCard(models.Model):
    i_num = models.CharField(max_length= 18)
    # False 代表女
    i_sex = models.BooleanField(default=False)
    i_person = models.OneToOneField(Person, on_delete=models.SET_NULL, null=True)


class Hobby(models.Model):
    h_name = models.CharField(max_length=16)
    h_cost = models.FloatField(default=1000)

    h_person = models.ForeignKey(Person, on_delete=models.PROTECT)

