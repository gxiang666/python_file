from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse


def hello(request):
    return HttpResponse("猴子请来的救兵")


def hello_doubing(request):
    print(request.META["REMOTE_ADDR"])
    return HttpResponse("豆兵")


def hehe_user(request,user_id):
    return HttpResponse("呵呵哒："+user_id)


def get_date(request,year,month,day):
    return HttpResponse("%s年%s月%s日" % (year,month,day))


def two(request):
    return render(request, 'two.html')


def wahaha(request):
    return render(request, 'wahaha.html')


def makequestion(request):
    # return HttpResponse('这个太简单了')
    # return HttpResponseRedirect("/four/wahaha")
    # return HttpResponseRedirect(reverse("two:haha"))
    # return HttpResponseRedirect("/four/getdate/4/1/2018/")
    # return HttpResponseRedirect(reverse("two:getdate", kwargs={"year":"2019","month":"11", "day":"11"}))
    return HttpResponseRedirect(reverse("two:hehe",args=('110',)))


def json_return(request):
    return JsonResponse({"msg":"ok","status":"200","data":"精神一下"})


def game(request):
    return render(request, '2048.html')
