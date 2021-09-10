from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('genre', views.genre, name='genre'),
    path('singer', views.singer, name='singer'),
    path('title', views.title, name='title'),
    ]