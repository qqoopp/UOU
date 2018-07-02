from django.conf.urls import include, url
from IOTMS.views import *
from django.urls import path
from django.contrib import admin

urlpatterns = [
    #path(r'', admin.site.urls),
    # url(r'^Postjson$', Postjson,name='Postjson'),
    # url(r'^Transdata$', Transdata,name='Transdata'),
    # url(r'^dashboard$', dashboard,name='dashboard'),
    # url(r'^dashboard_mpu$', dashboard_mpu,name='dashboard_mpu'),
    # url(r'^dashboard_dht$', dashboard_dht,name='dashboard_dht'),
    # url(r'^tservicereq$', dashboard_sound,name='dashboard_sound'),
    url(r'^ServiceReqInfo/(?P<qreqeustno>[A-Za-z0-9]+)', view=ServiceReqInfo),   
]


# #Add Django site authentication urls (for login, logout, password management)
# urlpatterns += [
#     path('accounts/', include('django.contrib.auth.urls')),
# ]