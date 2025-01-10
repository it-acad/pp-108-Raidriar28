
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authors/', include('author.urls')),
    path('books/', include('book.urls')),
    path('orders/', include('order.urls')),
    path('accounts/', include('authentication.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
]




