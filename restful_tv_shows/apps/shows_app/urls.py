from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^shows/$', views.index),
    url(r'^shows/new_show/$', views.new_show),
    url(r'^shows/view_show/(?P<id>[0-9]+)/$', views.view_show),
    url(r'^shows/edit_show_page/(?P<id>[0-9]+)/$', views.edit_show_page),
    url(r'^shows/edit_show/(?P<id>[0-9]+)/$', views.edit_show),
    url(r'^shows/delete_show/(?P<id>[0-9]+)/$', views.delete_show)
]