from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name ='blogApp-home'),
    path('about/', views.about, name='blogApp-about')
]
