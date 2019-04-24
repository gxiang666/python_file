import random

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from App.models import Dog, Person, IDCard, Hobby


def create_dog(request):
    # dog = Dog()
    # dog.d_name = "大黄"
    # dog.d_legs = 2
    flag = random.randrange(200)
    # dog = Dog.objects.create(d_name="大黄%d" % flag, d_legs=flag)
    dog = Dog.d_manager.create_model("中国田园犬")
    dog.is_delete = True
    dog.save()
    return HttpResponse("创建成功%d" % flag)


def get_dogs(request):
    # dogs = Dog.objects.filter(~Q(d_legs__lt=100))
    # dogs = Dog.d_manager.filter(Q(d_legs__lt=20)|Q(d_legs__gt=150))
    # dogs = Dog.d_manager.all().filter(is_delete=False)
    # dogs = Dog.d_manager.all()
    dogs = Dog.d_manager.filter(d_legs__lt=100)
    return render(request, 'DogList.html', context={"dogs": dogs})


def add_person(request):
    person = Person.objects.create(p_name="小黄%d"%random.randrange(110))
    person.save()
    return HttpResponse("创建小黄成功")


def add_id_card(request):
    id_card = IDCard()
    id_card.i_num = random.randrange(100000000000000000)
    person = Person.objects.last()
    id_card.i_person = person
    id_card.save()
    return HttpResponse("身份证绑定成功")


def delete_person(request):
    person = Person.objects.last()
    person.delete()
    return HttpResponse("删除成功")


def delete_id_card(request):
    id_card = IDCard.objects.last()
    id_card.delete()
    return HttpResponse("身份证删除成功")


def add_hobby(request):
    hobby = Hobby()
    flag = random.randrange(200)

    hobby.h_name = "Coding%d" % flag
    person = Person.objects.last()
    hobby.h_person = person
    hobby.save()
    return HttpResponse("爱好创建成功")


def delete_hobby(request):
    try:
        hobby = Hobby.objects.last()
        hobby.delete()
    except Exception as e:
        return HttpResponse(str(e))
    return HttpResponse("删除成功")


def getperson_and_idcard(request):
    person = Person.objects.last()
    # person = Person()
    idcard = person.idcard
    return HttpResponse(idcard.i_num)


def get_hobbies(request):
    # hobbies = Hobby.objects.filter(h_person_id=8)
    person = Person.objects.last()
    # person = Person()
    # hobby 和 query(objects) 是继承自相同的管理器的
    hobbies = person.hobby_set.filter(h_name='Coding141')
    return render(request, 'HobbyList.html', context={"hobbies": hobbies})
