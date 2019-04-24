import random

from django.http import HttpResponse
from django.shortcuts import render


# views 视图函数
from App.models import Person, Grade, Student


def hello(request):
    # 和数据库交互，逻辑判断，做一个返回
    # return HttpResponse("FirstPage")
    return render(request, "hello.html")


def first_page(request):
    # .return 快速生成返回语句
    return render(request, "first_page.html")


def person_list(request):
    # 拿到所有person
    persons = Person.objects.all()

    return render(request, "PersonList.html", context={"person_data": persons})


def person_add(request):
    # 添加人
    person = Person()
    person.p_name = "呵呵哒%d" % random.randrange(1000)
    person.p_age = 180
    # 存储
    person.save()
    return HttpResponse("添加成功%d" % person.id)


def grade_add(request):
    grade = Grade()
    grade.g_name = "python18%d" % random.randrange(200)
    grade.save()
    return HttpResponse("班级添加成功%d" % grade.id)


def student_add(request):
    # 拿最后一条
    grade = Grade.objects.last()
    student = Student()
    student.s_name = "你真是一个小天才%d" % random.randrange(200)
    student.s_age = 16
    student.s_grade = grade
    student.save()
    return HttpResponse("学生添加成功%d" % student.id)


def get_grade_list(request):
    grades = Grade.objects.all()
    return render(request, "GradeList.html", context={"grades":grades})


def get_students(request):
    students = Student.objects.all()
    return render(request, "StudentList.html", context={"students":students})