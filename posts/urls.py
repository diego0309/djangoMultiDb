from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index,  name='index'),
    path('nuevo', views.nuevo,  name='nuevo'),
    re_path(r'details/mysql/(?P<id>\d+)',
            views.detailsMySql,  name='detailsMySql'),
    re_path(r'details/sqlite/(?P<id>\d+)',
            views.detailsSqLite,  name='detailsSqLite'),
    re_path(r'details/mongo/(?P<id>\d+)',
            views.detailsMongo,  name='detailsMongo'),
]
