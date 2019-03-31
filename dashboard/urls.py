from django.contrib import admin
from django.urls import path, include
from . import views
from .views import index

app_name='dashboard'

urlpatterns = [
    path('', views.index, name="index"),
    path('charts/', views.charts, name="charts"),
    path('push/', views.push, name="push"),
    path('widgets/', views.widgets, name="widgets"),
    path('widgets/chatbot/' , views.chatbot , name = "chatbot")
]
