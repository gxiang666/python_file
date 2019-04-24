from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


# Mixin 多继承
class HelloMiddleware(MiddlewareMixin):

    def process_request(self, request):
        print(request.path)
        print(request.META['REMOTE_ADDR'])
        ip = request.META['REMOTE_ADDR']
        # if ip == '10.0.112.201':
        #     return HttpResponse("本网站不欢迎你")

        if request.path == '/app/getgoods/':
            username = request.POST.get("username")
            if username == "Rock":
                return HttpResponse("恭喜你抢到满1000减999的优惠券")
            elif ip == "10.0.112.42":
                return HttpResponse("优惠券已发放完毕")
            elif username == 'Tommy':
                return HttpResponse("优惠券已发放完毕")
            elif not username:
                return HttpResponse("请输入用户名")


    def process_exception(self, request, exception):
        print(str(exception))
        return redirect('/app/index/')
