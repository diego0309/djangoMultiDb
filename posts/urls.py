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
    re_path(r'details/cassandra/(?P<id>\d+)',
            views.detailsCassandra,  name='detailsCassandra'),    
    re_path(r'delete/sqlite/(?P<id>\d+)',
            views.deleteSqlite,  name='deleteSqLite'),
    re_path(r'delete/mysql/(?P<id>\d+)',
            views.deleteMysql,  name='deleteMysql'),
    re_path(r'delete/mongo/(?P<id>\d+)',
            views.deleteMongo,  name='deleteMongo'),
    re_path(r'delete/cassandra/(?P<id>\d+)',
            views.deleteCassandra,  name='deleteCassandra'),    
]
