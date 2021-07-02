from django.contrib import admin
from django.urls import path, include
from Customer_details import views

urlpatterns = [
    path('', views.FETCH),
    path('output/', views.SHOW)
]
