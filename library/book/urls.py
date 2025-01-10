from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('<int:book_id>/', views.book_detail, name='book_detail'),
    path('create/', views.create_book, name='create_book'),
    path('<int:book_id>/update/', views.update_book, name='update_book'),
    path('<int:book_id>/delete/', views.delete_book, name='delete_book'),
    path('by-user/<int:user_id>/', views.books_by_user, name='books_by_user'),
]



