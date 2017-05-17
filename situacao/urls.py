from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.situacao, name='situacao'),
    url(r'^add/$', views.add, name='situacao.add'),
    url(r'^(?P<id>[0-9]+)/$', views.detail, name='situacao.detail'),
]


