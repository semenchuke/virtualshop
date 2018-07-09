from django.urls import re_path
import authapp.views as authapp


app_name = 'authapp'

urlpatterns = [
    re_path(r'^login/$', authapp.login, name = 'login'),
    re_path(r'^registr/$', authapp.registr, name = 'registr'),
    re_path(r'^logout/$', authapp.logout, name = 'logout'),
    re_path(r'^edit/$', authapp.edit, name = 'edit'),
]