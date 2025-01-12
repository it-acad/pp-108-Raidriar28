from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm
from django.shortcuts import redirect
from django.http import HttpResponseNotFound
def book_list(request):
    query = request.GET.get('q')
    books = Book.objects.all()
    if query:
        books = books.filter(name__icontains=query)
    return render(request, 'book/book_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book/book_detail.html', {'book': book})

def books_by_user(request, user_id):
    from order.models import Order
    orders = Order.objects.filter(user_id=user_id, end_at=None)
    books = [order.book for order in orders]
    return render(request, 'book/books_by_user.html', {'books': books})

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book:book_list')
    else:
        form = BookForm()
    return render(request, 'book/create_book.html', {'form': form})

def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book:book_detail', book_id=book.id)
    else:
        form = BookForm(instance=book)
    return render(request, 'book/update_book.html', {'form': form, 'book': book})

def delete_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        book.delete()
        return redirect('book:book_list')
    except Book.DoesNotExist:
        return HttpResponseNotFound("None book with this ID.")

# def delete_book(request, book_id):
#     book = Book.objects.filter(id=book_id).first()
#     if not book:
#         return redirect('book:book_list')
#     book.delete()
#     return redirect('book:book_detail', book_id=book.id)

