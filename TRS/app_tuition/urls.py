from django.urls import path
from app_tuition import views

app_name = 'app_tuition'

urlpatterns = [
    path('', views.home, name='home'),
    path('api_get_year_tuition/', views.api_get_year_tuition, name='api_get_year_tuition'),
]