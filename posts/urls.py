from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index,  name='index'),
    path('nuevo', views.nuevo,  name='nuevo'),
    re_path(r'details/(?P<id>\d+)', views.details,  name='details'),
]
