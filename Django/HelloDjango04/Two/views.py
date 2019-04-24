import random

from django.http import HttpResponse
from django.shortcuts import render

from Two.models import Buyer, Goods, Cat, Dog


def add_person(request):
    flag = random.randrange(200)
    p = Buyer.objects.create(b_name="清醒%d下" % flag)
    p.save()
    return HttpResponse('创建成功%d' % flag)


def add_goods(request):
    flag = random.randrange(300)
    goods = Goods.objects.create(g_name="娃娃%d" % flag, g_price=flag)
    goods.save()
    return HttpResponse("商品上架成功")


def add_goods_to_buyer(request):
    goods = Goods.objects.last()
    buyer = Buyer.objects.last()
    # goods = Goods()
    # 集合
    goods.g_buyers.add(buyer)
    goods.save()
    return HttpResponse("剁手成功")


def get_buyer_from_goods(request):
    goods = Goods.objects.last()
    # goods = Goods()
    buyers = goods.g_buyers.all()
    return render(request, 'BuyerList.html', context={"buyers": buyers})


def get_goods_from_buyer(request):
    buyer = Buyer.objects.last()
    # buyer = Buyer()
    goods_list = buyer.goods_set.all()
    return render(request, 'GoodsList.html', context={"goodslist":goods_list})


def delete_goods(request):
    goods = Goods.objects.last()
    goods.delete()
    return HttpResponse("成功清除")


def delete_buyer(request):
    buyer = Buyer.objects.last()
    buyer.delete()
    return HttpResponse("成功删除薅羊毛的用户")


def add_cat(request):
    cat = Cat()
    cat.a_name = "汤姆猫"
    cat.c_fun = "被老鼠抓"
    cat.save()
    return HttpResponse("成功创建小猫")


def add_dog(request):
    dog = Dog()
    dog.a_name = "牧羊犬"
    dog.d_fun = "看羊"
    dog.save()
    return HttpResponse("成功创建小狗")