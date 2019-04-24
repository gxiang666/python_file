from django.conf.urls import url

from Two import views

urlpatterns = [
    url(r'^two/', views.two),
    url(r'^gradeadd/', views.grade_add),
    url(r'^studentadd/', views.student_add),
    url(r'^studentget/', views.student_get),
    url(r'^gradeget/', views.grade_get),
    url(r'^getgrade/', views.get_grade),
    url(r'^avg/', views.get_avg),
]