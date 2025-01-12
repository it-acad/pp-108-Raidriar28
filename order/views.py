from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import now
from .models import Order
from django.contrib.auth.decorators import login_required

@login_required
def order_list(request):
    if request.user.role == 1:  # Librarian
        orders = Order.objects.all()
    else:
        orders = Order.objects.filter(user=request.user)  # User sees only their orders
    return render(request, 'orders/order_list.html', {'orders': orders})

@login_required
def create_order(request):
    if request.method == 'POST':
        user_id = request.POST.get('user')
        book_id = request.POST.get('book')
        plated_end_at = request.POST.get('plated_end_at')
        from authentication.models import CustomUser  # Локальный импорт
        from book.models import Book  # Локальный импорт
        user = get_object_or_404(CustomUser, pk=user_id)
        book = get_object_or_404(Book, pk=book_id)

        if book.count > 0:
            order = Order.objects.create(user=user, book=book, plated_end_at=plated_end_at)
            if order:
                book.count -= 1
                book.save()
        return redirect('order_list')

    from authentication.models import CustomUser  # Локальный импорт
    from book.models import Book  # Локальный импорт
    users = CustomUser.objects.all()
    books = Book.objects.filter(count__gt=0)
    return render(request, 'orders/create_order.html', {'users': users, 'books': books})

@login_required
def close_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order.end_at = now()
    order.book.count += 1
    order.book.save()
    order.save()
    return redirect('order_detail', order_id=order.id)





