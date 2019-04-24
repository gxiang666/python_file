import hashlib
import random

import os
import uuid

from PIL import Image, ImageDraw, ImageFont
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

from App.models import UserModel
from Day07 import settings


def index(request):
    return HttpResponse("首页")


def home(request):
    return HttpResponse("回家")


def goods(request):
    return render(request, 'Goods.html')


def get_goods(request):

    rand = random.randrange(100)

    if rand > 90:
        return HttpResponse("恭喜你抢到了满100减99的优惠券")
    else:
        return HttpResponse("很遗憾你没有抢到，可以再试一次")


def cal(request):

    rand = random.randrange(200)

    if rand > 20:
        n = 1 /0
        print(n)

    return HttpResponse('计算成功，你的智商是180')


def upload(request):
    return render(request, 'upload.html')


def do_upload(request):

    # username = request.POST.get("username")
    #
    # print(request.FILES)
    # icon = request.FILES['icon']
    #
    # user = UserModel()
    # user.u_name = username
    # user.u_icon = icon
    # user.save()


    # 手动处理文件上传
    icon = request.FILES['icon']

    file_out_path = os.path.join(settings.MEDIA_ROOT, generate_filename()+".png")

    with open(file_out_path, 'wb') as saveicon:
        for part in icon.chunks():
            saveicon.write(part)
            saveicon.flush()

    return HttpResponse("保存成功")


def get_user_info(request, id):

    user = UserModel.objects.get(pk=id)

    print(user.u_icon)

    print(user.u_icon.url)

    print(user.u_icon.path)

    uicon = '/static/upload/'+user.u_icon.url

    data = {
        'u_icon': uicon,
        'u_name': user.u_name,
    }

    return render(request, 'userinfo.html', context=data)

def generate_filename():

    u = uuid.uuid4()
    u = str(u)
    md5 = hashlib.md5()
    md5.update(u.encode('utf-8'))

    return md5.hexdigest()


def get_users(request, page_num):

    users = UserModel.objects.all()

    paginator = Paginator(users, 3)

    page = paginator.page(page_num)

    object_list = page.object_list

    data = {
        'users': object_list,
        'page_range': paginator.page_range,
        'page': page,
    }

    return render(request, 'userlist.html', context=data)


def get_verify_code(request):

    # 画布
    size = (100, 50)
    color = get_color()
    image = Image.new("RGB",size, color)

    # 画笔
    imagedraw = ImageDraw.Draw(image, "RGB")

    # 字体
    imagefont = ImageFont.truetype('/home/rock/Python1801/DjangoDay07/Day07/static/fonts/ADOBEARABIC-BOLDITALIC.OTF', 30)

    source = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"

    verify = ""

    for i in range(4):
        # 每循环一次获取一个字母
        verify += source[random.randrange(len(source))]

    print(verify)
    request.session['verify_code'] = verify

    for item in range(4):
        imagedraw.text((10 + 20*item,10),verify[item], fill=get_color(), font=imagefont)

    # 画布中封装了绘制的相关API
    # imagedraw.text((25, 10), 'M', font=imagefont, fill=get_color())
    # imagedraw.text((50, 10), 'a', font=imagefont)
    # imagedraw.text((75, 10), 'c', font=imagefont)

    for item in range(500):
        imagedraw.point(get_point(), fill=get_color())


    import io
    # 开辟 io 缓冲区
    buf = io.BytesIO()
    # 将图片写入缓冲区

    image.save(buf, 'png')

    return HttpResponse(buf.getvalue(),"image/png")


def get_color():

    red = random.randrange(256)
    green = random.randrange(256)
    blue = random.randrange(256)

    return (red, green, blue)


def get_point():
    width = random.randrange(100)
    height = random.randrange(50)
    return (width, height)


def user_login(request):
    return render(request, 'UserLogin.html')


def do_user_login(request):
    verify_code = request.POST.get("username")

    verify = request.session.get('verify_code')

    if verify_code == verify:

        return HttpResponse("验证成功")
    else:
        return redirect('/app/userlogin/')