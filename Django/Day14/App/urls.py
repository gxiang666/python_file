from django.conf.urls import url

from App.views import HelloView, UserView, HelloTemplateView, HelloRedirectView

urlpatterns = [
    url(r'^hello/', HelloView.as_view(), name='hello'),
    url(r'^user/', UserView.as_view(), name='user'),
    url(r'^template/', HelloTemplateView.as_view(), name='template'),
    url(r'^redirect/', HelloRedirectView.as_view(), name='redirect'),
]