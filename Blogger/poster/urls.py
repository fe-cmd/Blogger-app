from atexit import register
from unicodedata import name
from django.urls import path
from .import views

urlpatterns = [
    path('begin', views.index, name='index'),
    path('post/<str:pk>', views.post, name='post'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('home', views.home, name='home'),
    path('contact', views.contact, name='contact')
]
