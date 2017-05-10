from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.escolaridade, name='escolaridade'),
    url(r'^(?P<id>[0-9]+)/$', views.detail, name='escolaridade.detail'),
    url(r'^escolaridade/add/$', views.add, name='escolaridade.add'),
]