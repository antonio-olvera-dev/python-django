from django.urls import path

from . import views

users =  views.Users

urlpatterns = [
    path('', users.index, name='index'),
    path('user', users.user, name='user'),
]