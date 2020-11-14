from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('home/', views.home),
    path('save/',views.save_data,name="save"),
    path('delete/',views.delete_data,name="delete"),
    path('edit/',views.edit_data,name="edit")
]