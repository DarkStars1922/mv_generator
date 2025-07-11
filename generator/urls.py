from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('generate/', views.generate_mv, name='generate_mv'),
    path('result/', views.mv_result, name='mv_result'),
]
