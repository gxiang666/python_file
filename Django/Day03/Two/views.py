import random

from django.db.models import Avg, Max, F
from django.http import HttpResponse
from django.shortcuts import render

from Two.models import Grade, Student


def two(request):
    return HttpResponse("小伙子别睡了")


def grade_add(request):
    grade = Grade()
    grade.g_name = "python%d" % random.randrange(200)
    grade.save()
    return HttpResponse("创建成功%d" % grade.id)


def student_add(request):
    student = Student()
    flag = random.randrange(300)
    student.s_name = "小黄%d" % flag
    student.s_age = flag
    grade = Grade.objects.last()
    student.s_grade = grade
    student.save()
    return HttpResponse("学生创建%d" % student.id)


def grade_get(request):
    grades = Grade.objects.all()
    return render(request, "GradeList.html", context={"grades": grades})

"""
    1. 有一个视图函数，可以获取所有班级
    2. 有一个视图函数，可以获取所有学生
    3. 有一个链接，可以跳转到学生页面
    4. 跳转到学生页面，要对学生进行班级筛选
        跳转的时候将班级的唯一标识传递  get参数形式

"""
def student_get(request):
    gradeid = request.GET.get("gradeid")
    print(gradeid)
    # students = Student.objects.filter(s_grade_id=gradeid)

    students = Student.objects.filter(s_grade_id__gt=F('id')-5)
    return render(request, 'StudentList.html', context={"students": students})


def get_grade(request):
    grades = Grade.objects.filter(student__s_name="小黄9")
    return render(request, "GradeList.html", context={"grades": grades})


def get_avg(request):
    result = Student.objects.aggregate(Max('s_age'))
    print(result)
    return HttpResponse("计算成功")
