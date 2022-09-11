from django.contrib import admin
from django.urls import path
from books.views import LoginView, RegisterView, view_books
from .import views


urlpatterns = [
    path('view_books', views.view_books, name ='view_books'),
    path('add-books', views.add_book, name ='view-books'),
    path('delete-books/<str:id>/', views.delete_book, name='delete-books'),
    path('update-books/<str:id>/', views.update_books, name='update-books'),
    # api call for updatation  
    path('book-update/<str:pk>/',views.bookupdate, name='book-update/'),
    # api for creating the book 
    path('book-create/',views.bookcreate, name='book-create/'),
    # api call for deleting the book
    path('book-delete/', views.bookdelete, name='book-delete')
]
