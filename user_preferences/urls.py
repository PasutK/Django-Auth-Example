from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.UserLogin, name="login"),
    path('logout/', views.UserLogout, name="logout"),
    path('add-new-teacher/', views.AddNewTeacher, name="add_new_teacher"),
]