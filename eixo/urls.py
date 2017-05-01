from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='eixo'),
    url(r'^(?P<eixo_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^add/$', views.add, name='add'),
]