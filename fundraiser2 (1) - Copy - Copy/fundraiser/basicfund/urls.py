from django.urls import path
from . import views

urlpatterns=[
    path('', views.home),
    path('profile/', views.profile),
    path('login/', views.login),
    path('join/', views.join),
    path('about/', views.about),
    path('kristina/', views.kristina),
    path('marie/', views.marie),
    path('donate/', views.donate1),
    path('lynsey/', views.lynsey),
    path('stuart/', views.stuart),
    path('domi/', views.domi),




    # path('home', views.home)
]