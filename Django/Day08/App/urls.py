from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^getperson/', views.get_person),
    url(r'^getstudents/', views.get_students),
    url(r'^gettinymce/', views.get_tinymce),
]