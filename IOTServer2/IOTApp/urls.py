from django.conf.urls import include, url
from IOTApp.views import *
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path(r'', admin.site.urls),
    url(r'^Postjson$', Postjson,name='Postjson'),
    url(r'^Transdata$', Transdata,name='Transdata'),
    url(r'^dashboard$', dashboard,name='dashboard'),
    url(r'^dashboard2$', dashboard2,name='dashboard2'),
    url(r'^dashboard_fire$', dashboard_fire,name='dashboard_fire'),
    url(r'^dashboard_dht$', dashboard_dht,name='dashboard_dht'),
    url(r'^dashboard_light$', dashboard_light,name='dashboard_light'),
    url(r'^dashboard_guage$', dashboard_guage,name='dashboard_guage')
]

