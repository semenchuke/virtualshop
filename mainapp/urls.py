from django.contrib import admin
from django.urls import re_path
import mainapp.views as mainapp


app_name = 'mainapp'

urlpatterns = [
    re_path('^$', mainapp.catalog, name = 'catalog'),
    re_path('^oculusrift', mainapp.oculus_rift, name = 'oculus'),
    re_path('^psvr', mainapp.psvr, name = 'psvr'),
    re_path('^htcvive/', mainapp.htc_vive, name = 'htc_vive'),
    re_path('^halolens/', mainapp.halolens, name='halolens'),
    re_path(r'^category/(?P<category_pk>\d+)/$', mainapp.catalog, name='category'),
    re_path(r'product/(?P<pk>\d+)/$', mainapp.product, name = 'product'),
]