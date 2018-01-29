from django.urls import path

from . import views

urlpatterns = [
    path('borrowings/', views.borrowings, name='borrowings'),
    path('books/', views.books, name='books'),
    path('readers/', views.readers, name='readers'),
    path('', views.index, name='index'),
]
