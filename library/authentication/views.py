from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        middle_name = request.POST.get('middle_name')
        role = request.POST.get('role')

        if email and password:
            CustomUser.objects.create_user(
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                middle_name=middle_name,
                role=role,
            )
            return redirect('login')
    return render(request, 'authentication/register.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            if user.role == 1:  # Librarian
                return redirect('user_list')
            return redirect('book_list')
    return render(request, 'authentication/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def user_list(request):
    if request.user.role != 1:
        return redirect('book_list')  # Only librarians can access
    users = CustomUser.objects.all()
    return render(request, 'authentication/user_list.html', {'users': users})


@login_required
def user_detail(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    if request.user.role != 1 and request.user.id != user_id:
        return redirect('book_list')  # Only librarians or the user themselves can access
    return render(request, 'authentication/user_detail.html', {'user': user})
