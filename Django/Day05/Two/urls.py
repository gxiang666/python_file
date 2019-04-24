from django.conf.urls import url

from Two import views

urlpatterns = [
    url(r'^hello/', views.hello),
    url(r'^hellodoubing/', views.hello_doubing),
    url(r'^hehe/(\d+)/', views.hehe_user, name='hehe'),
    url(r'^getdate/(?P<month>\d+)/(?P<day>\d+)/(?P<year>\d+)', views.get_date, name='getdate'),
    url(r'^two/', views.two),
    url(r'^wahaha/', views.wahaha, name='haha'),
    url(r"^makequestion/", views.makequestion),
    url(r'^jsonreturn/', views.json_return),
    url(r'^game/', views.game),
]