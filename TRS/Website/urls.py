from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('dbsearch/' , views.dbsearch),
    path('showlist/' , views.showlist , name='showlist'),
]