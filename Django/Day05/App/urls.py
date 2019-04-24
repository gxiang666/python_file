from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^hello/', views.hello),
    url(r'^getanimals/', views.get_animals),
    url(r'^getanimalstwo/', views.get_animals_two),
    url(r'^index/', views.index),
    url(r'^indextwo/', views.index_two),
    url(r'^indexthree/', views.index_three),

]