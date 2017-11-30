from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^helloworld$', views.hello, name='hello'),
    url(r'^list$',views.list, name='list'),
    url(r'^add$',views.add, name='add'),
    url(r'^edit$',views.edit, name='edit'),
    url(r'^delete$',views.delete, name='delete'),
    url(r'^(?P<article_id>[0-9]+)$', views.detail, name='detail'),
    url(r'^toadd$', views.toadd, name='toadd'),
    url(r'^toedit/(?P<article_id>[0-9]+)$', views.toedit, name='toedit'),
    url(r'^search$', views.search, name='search')
]