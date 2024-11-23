from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('get_books/', views.get_book, name='get_book'),
    path('create_books/', views.create_book, name='create_book'),
    path('edit_book/', views.edit_book, name='edit_book'),
    
]
