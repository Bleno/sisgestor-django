from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='unidade'),
    url(r'^add$', views.add, name='unidade.add'),
    url(r'^(?P<unidade_id>[0-9]+)/$', views.detail, name='unidade.detail'),
]