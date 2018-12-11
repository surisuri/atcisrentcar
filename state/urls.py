from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.listcar, name='listcar'),
    #url(r'^state/(?P<pk>\d+)/$', views., name='post_detail'),
]