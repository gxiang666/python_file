from time import sleep

from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.decorators.cache import cache_page

from App.models import Student


def index(request):
    return HttpResponse("这是首页")


@cache_page(60)
def get_person(request):

    sleep(10)

    return HttpResponse("你要找的人费了九牛二虎之力找到了，请付酬劳100w")


def get_students(request):
    students_cache = cache.get('get_students')
    if students_cache:
        # 有数据
        result = students_cache
    else:
        # 没有数据
        students = Student.objects.all()
        sleep(5)
        data = {
            "students": students,
        }
        template = loader.get_template('student_list.html')
        result = template.render(data)
        cache.set('get_students', result, 60)

    return HttpResponse(result)


def get_tinymce(request):
    return render(request, 'RTF.html')
