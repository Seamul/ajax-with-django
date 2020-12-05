from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('upload/', views.uploadFile,name="upload"),
    # path('save/',views.save_data,name="save"),
    # path('delete/',views.delete_data,name="delete"),
    # path('edit/',views.edit_data,name="edit")
]