import time
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, RedirectView

from App.models import UserModel

"""
    视图函数
    
    类视图
        继承View

"""
class HelloView(View):

    def get(self, request):

        return HttpResponse("这是类视图的Get请求")


class UserView(View):

    def get(self, request):

        time.sleep(5)

        return render(request, 'UserRegister.html')

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")

        # user = UserModel()
        user = UserModel.objects.create(username=username, password=password, email=email)
        user.save()
        request.session["user_id"] = user.id

        data = {
            "user_id": user.id,
        }

        return render(request, "Userinfo.html", context=data)

    def put(self, request):

        return HttpResponse("PUT Supported")


def user_register(request):
    if request.method == "GET":
        return render(request, 'UserRegister.html')
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")

        # user = UserModel()
        user = UserModel.objects.create(username=username, password=password, email=email)
        user.save()
        request.session["user_id"] = user.id

        data = {
            "user_id": user.id,
        }

        return render(request, "Userinfo.html", context=data)


class HelloTemplateView(TemplateView):

    template_name = "UserLogin.html"

    def post(self, request):

        username = request.POST.get("username")
        password = request.POST.get("password")

        return HttpResponse(username)


class HelloRedirectView(RedirectView):

    # url = '/app/template/'
    pattern_name = "app:user"