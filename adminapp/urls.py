from django.urls import re_path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    re_path(r'^$', adminapp.main, name='main'),
    re_path(r'^user/create/$', adminapp.user_create, name='user_create'),
    re_path(r'^user/update/(?P<pk>\d+)/$', adminapp.user_update, name='user_update'),
    re_path(r'^user/delete/(?P<pk>\d+)/$', adminapp.user_delete, name='user_delete'),

    re_path(r'^categories/$', adminapp.categories, name='categories'),
    re_path(r'^categories/create/$', adminapp.category_create, name='category_create'),
    re_path(r'^categories/update/(?P<pk>\d+)/$', adminapp.category_update, name='category_update'),
    re_path(r'^categories/delete/(?P<pk>\d+)/$', adminapp.category_delete, name='category_delete')
]
