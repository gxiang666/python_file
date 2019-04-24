from django.conf.urls import url

from Two import views

urlpatterns = [
    url(r'^addperson/', views.add_person),
    url(r'^addgoods/', views.add_goods),
    url(r'^addtobuyer/', views.add_goods_to_buyer),
    url(r'^delbuyer/', views.delete_buyer),
    url(r'^delgoods/', views.delete_goods),
    url(r'^getbuyers/', views.get_buyer_from_goods),
    url(r'^getgoods/', views.get_goods_from_buyer),
    url(r'^addcat/', views.add_cat),
    url(r'^adddog/', views.add_dog),
]