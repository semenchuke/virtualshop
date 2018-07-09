from django.urls import re_path
import basketapp.views as basketapp


app_name = 'basketapp'

urlpatterns = [
    re_path('^$', basketapp.basket, name = 'watch_in'),
    re_path('^add/(?P<pk>\d+)/$', basketapp.add, name = 'add'),
    re_path('^remove/(?P<pk>\d+)/$', basketapp.remove, name = 'remove'),
    re_path('^edit/(?P<pk>\d+)/(?P<value>\d+)/$', basketapp.edit),
]