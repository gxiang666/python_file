import hashlib
import random
import time
import uuid

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from App.models import UserModel


def hello(request):

    print(request.path)

    print(request.method)

    print(request.GET)

    print(request.GET.get("name","游客"))

    print(request.GET.getlist('name'))

    # print(request.GET["name"])

    print(request.POST)

    response = HttpResponse()

    response.content = "最近几天都是严重空气污染"
    # response.status_code = 404

    response.write("谢谢谢")
    response.flush()

    return response

    # return HttpResponse("为啥你这么困？")


def post_form(request):
    return render(request, 'post_form.html')


def chongdingxiang(request):
    # return HttpResponseRedirect(reverse('app:post_form'))
    # return HttpResponseRedirect('/app/postform/')
    return redirect(reverse('app:post_form'))


def index(request):
    uname = request.session.get('uname')
    data = {
        "username": uname
    }
    return render(request, 'index.html',context=data)


def login(request):
    return render(request, 'login.html')


def do_login(request):
    response = HttpResponse("登录成功")

    username = request.POST.get("username")

    request.session['uname'] = username
    # response.set_cookie("uname", username, max_age=30)
    # response.set_cookie("uname", username, expires=timedelta(minutes=1))

    return response


def logout(request):
    response = HttpResponse("退出成功，欢迎再来")

    # response.delete_cookie("sessionid")

    # del request.session['uname']
    #  同时清除cookie 和 session
    request.session.flush()

    return response


def user_register(request):
    return render(request, 'user_register.html')


def do_user_register(request):
    u_name = request.POST.get('username')
    u_password = request.POST.get('password')
    u_age = request.POST.get('age')
    user = UserModel()
    user.u_name = u_name
    user.u_password = password_sec(u_password)
    user.u_age = u_age

    # u_token 唯一标识
    # 时间 + 随机数 + 公司域名 + ip信息
    # 时间 + 域名
    token = generate_token()
    user.u_token = token
    user.save()
    response = HttpResponseRedirect(reverse("app:user_info"))
    response.set_cookie("utoken", token)
    return response


def password_sec(password):

    md5 = hashlib.md5()
    md5.update(password.encode("utf-8"))
    return md5.hexdigest()


def generate_token():
    # token = str(time.time()) + str(random.random())

    token = str(uuid.uuid4())

    print(token)

    md5 = hashlib.md5()
    # 默认md5 输出128位的二进制，十六进制和二进制转换， 32位的十六进制， 一个16进制就可以转换成一个字符
    # 将元数据，传入算法中
    md5.update(token.encode("utf-8"))
    # 获取十六进制摘要
    token = md5.hexdigest()

    return token


def get_user_info(request):
    utoken = request.COOKIES.get("utoken")
    user = None
    if utoken:
        users = UserModel.objects.filter(u_token=utoken)
        if users.exists():
            user = users.first()

    return render(request, 'UserInfo.html', context={"user" : user})


def user_login(request):
    if request.method == "GET":
        return render(request, 'user_login.html')
    else:
        u_name = request.POST.get("username")
        u_password = request.POST.get("password")
        users = UserModel.objects.filter(u_name=u_name)
        if users.exists():
            user = users.first()
            if user.u_password == password_sec(u_password):
                token = generate_token()
                user.u_token = token
                user.save()
                response = redirect(reverse("app:user_info"))
                response.set_cookie("utoken", user.u_token)
                return response
            # else:
            #     return HttpResponse("密码错误")

        # return HttpResponse("用户名不存在")
        return HttpResponse("用户或密码错误")