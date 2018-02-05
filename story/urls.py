from django.urls import path

from . import views

urlpatterns = [
    path('story/',views.home_page),
    path('', views.index, name='index'),
]