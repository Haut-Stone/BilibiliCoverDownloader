# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2017-06-13 19:50:42
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2017-07-10 11:41:42

from django.conf.urls import url
from .import views

app_name = 'Downloader'

urlpatterns = [
	url(r'^helloPage/$', views.helloPage, name = 'helloPage'),
	url(r'^loadPage/$', views.loadPage, name = 'loadPage'),
	url(r'^iosPage/(?P<target>[0-9]+)/$', views.iosPage, name = 'iosPage'),
]