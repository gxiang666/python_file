import random

from django.http import HttpResponse
from django.shortcuts import render

from App.models import Animal, Flower


def animal_add(request):
    animal = Animal()
    animal.a_name = "Cat"
    animal.a_legs = 4
    animal.save()
    return HttpResponse("Add Success")


def animal_get(request):
    animals = Animal.objects.all()
    return render(request,'AnimalList.html',context={"animals":animals})


# 数据删除和数据修改都是基于查询的
def animal_mod(request):
    animal = Animal.objects.last()

    animal.a_legs = 5
    animal.save()
    return HttpResponse("修改成功")


def animal_del(request):
    animal = Animal.objects.last()
    # None
    animal.delete()
    return HttpResponse("删除成功")


def flower_add(request):
    flower = Flower()
    flag = random.randrange(200)
    flower.f_name = "狗尾巴花%d" % flag
    flower.f_color = flag
    flower.save()
    return HttpResponse("鲜花创建成功%d" % flag)


def flower_get(request):
    # flowers = Flower.objects.all()
    # flowers = Flower.objects.filter(f_color__gt=100).filter(f_color__lt=150)
    # flowers = Flower.objects.filter(f_color__gt=100).exclude(f_color__gt=150).filter(f_name__contains="水")
    # flowers = Flower.objects.filter(f_name__endswith="1")
    # flowers = Flower.objects.filter(f_name="rose")
    # 如果排序字段是字符串   默认排序方式 字典排序  a  aa   ab   b  ac
    # flowers = Flower.objects.all().order_by("-id")[0:2]

    # flowers = Flower.objects.filter(pk__in=[1,2,3,4])
    flowers = Flower.objects.filter(f_time__year="2019")
    print(type(flowers))
    print(flowers.values())
    return render(request, 'FlowerList.html', context={"flowers": flowers})


def flower_get_single(request):
    # get 要慎用，一个都不反会跑出异常 不存在，返回多个也会抛出异常，multiobjectsreturned
    # flower=Flower.objects.get(pk=10)
    # flower = Flower.objects.get(f_color=255)
    flowers = Flower.objects.filter(f_color=255)
    # flower = flowers.last()
    # flower = flowers.first()
    # if flowers.count() == 0:
    #     return HttpResponse("所查询的鲜花不存在")
    # flower = flowers.first()

    if flowers.exists():
        flower = flowers.first()
        return HttpResponse(flower.f_name)
    else:
        return HttpResponse("鲜花都卖没了")
