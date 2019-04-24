from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^animalmod/', views.animal_mod),
    url(r'^animaldel/', views.animal_del),
    url(r'^floweradd/', views.flower_add),
    url(r'^flowerget/', views.flower_get),
    url(r'^flowersingle/', views.flower_get_single),
]