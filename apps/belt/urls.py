from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='success'),
    url(r'^add/friend/(?P<id>\d+)$', views.add, name='add-friend'),
    url(r'^view/friend/(?P<id>\d+)$', views.show, name='view-friend'),
    url(r'^remove/friend/(?P<id>\d+)$', views.remove, name='remove-friend')
]
