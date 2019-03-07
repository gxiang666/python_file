from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse


def hello(request):
    return HttpResponse("hello world")


def homeproc(request):
    response = HttpResponse()
    response.write('<h1>这是首页<a href="http://www.baidu.com">点击跳转百度</a></h1>')
    response.write("<h1>dierhang</h1>")
    return response


def homeproc1(request):
    response = JsonResponse({'key': 'value'})
    return response
