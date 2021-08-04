from django.contrib import admin
from django.urls import path, include

from upload_image import views

urlpatterns = [
    path('index', views.index),
]
