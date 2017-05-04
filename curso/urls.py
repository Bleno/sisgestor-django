from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.curso, name='curso'),
	url(r'^(?P<curso_id>[0-9]+)/$', views.detail, name='curso.detail'),
	url(r'^add/$', views.add, name='curso.add'),
]


