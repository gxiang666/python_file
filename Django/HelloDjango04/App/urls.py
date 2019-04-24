from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^createdog/', views.create_dog),
    url(r'^getdogs/', views.get_dogs),
    url(r'^addperson/', views.add_person),
    url(r'^addidcard/', views.add_id_card),
    url(r'^delperson/', views.delete_person),
    url(r'^delidcard/', views.delete_id_card),
    url(r'^addhobby/', views.add_hobby),
    url(r'^delhobby/', views.delete_hobby),
    url(r'^getpersonandidcard/', views.getperson_and_idcard),
    url(r'^gethobbies/', views.get_hobbies),
]