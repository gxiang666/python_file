from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^home/', views.home),
    url(r'^goods/', views.goods),
    url(r'^getgoods/', views.get_goods, name='get_goods'),
    url(r'^cal/', views.cal),
    url(r'^upload/', views.upload),
    url(r'^doupload/', views.do_upload, name='do_upload'),
    url(r'^getuserinfo/(\d+)/', views.get_user_info),
    url(r'^getusers/(\d+)/', views.get_users, name='get_users'),
    url(r'^getverifycode', views.get_verify_code),
    url(r'^userlogin/', views.user_login),
    url(r'^douserlogin/', views.do_user_login),
]