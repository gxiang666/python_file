from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^hello/', views.hello, name='hello'),
    url(r'^postform/', views.post_form, name='post_form'),
    url(r'^chongdingxiang/', views.chongdingxiang),
    url(r'^index/', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^dologin/', views.do_login, name='do_login'),
    url(r'^logout/', views.logout, name='logout'),

    url(r'^userregister/', views.user_register, name='user_register'),
    url(r'^douserregister/', views.do_user_register, name='do_user_register'),
    url(r'^userinfo/', views.get_user_info, name='user_info'),
    url(r'^userlogin/', views.user_login, name='user_login'),
]