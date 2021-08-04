from django.contrib import admin
from django.urls import path, include

from nlp import views

urlpatterns = [
    path('chat', views.chat),
]
