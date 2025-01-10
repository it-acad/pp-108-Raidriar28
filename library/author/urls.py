from django.urls import path
from . import views

app_name = 'author'

urlpatterns = [
    path('', views.author_list, name='author_list'),
    path('create/', views.create_author, name='create_author'),
    path('<int:author_id>/', views.author_detail, name='author_detail'),
    path('<int:author_id>/update/', views.update_author, name='update_author'),
    path('<int:author_id>/delete/', views.delete_author, name='delete_author'),
]
