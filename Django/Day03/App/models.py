from django.db import models


class Animal(models.Model):
    a_id = models.AutoField(primary_key=True)
    a_name = models.CharField(max_length=32, unique=True)
    a_legs = models.IntegerField(default=4)
    is_delete = models.BooleanField(default=False)


class Flower(models.Model):
    f_name = models.CharField(max_length=32)
    f_color = models.IntegerField(default=0, db_column="color")
    f_time = models.DateTimeField(auto_now=True)

    def get(self):
        return "德玛西亚"

    # 元信息
    class Meta:
        db_table = 'Flower'
        ordering = ["-f_color"]
