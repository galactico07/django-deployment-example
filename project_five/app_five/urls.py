from django.contrib import admin
from django.urls import path
from app_five import views

app_name = 'app_five'

urlpatterns = [
    path('home',views.index,name='home'),
    path('login',views.user_login,name ='user_login'),
    path('registration',views.registrations,name = 'registration'),
    path('registration2',views.registrations2,name = 'registration2'),
]
