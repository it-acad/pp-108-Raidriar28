from django.shortcuts import render, get_object_or_404, redirect
from .models import Author
from django.http import Http404
def author_list(request):
    """
    Display a list of all authors.
    """
    authors = Author.objects.all()
    return render(request, 'authors/author_list.html', {'authors': authors})


def create_author(request):
    """
    Create a new author.
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        patronymic = request.POST.get('patronymic')
        if name and surname and patronymic:
            Author.create(name=name, surname=surname, patronymic=patronymic)
            return redirect('author:author_list')
    return render(request, 'authors/create_author.html')


def delete_author(request, author_id):
    """
    Delete an author if they are not associated with any books.
    """
    try:
        author = Author.objects.get(pk=author_id)
        if not author.books.exists():  # Check if the author is not linked to any books
            author.delete()
            return redirect('author:author_list')
        else:
            return render(request, 'authors/error.html', {'message': 'Cannot delete author linked to books.'})
    except Author.DoesNotExist:
        return render(request, 'authors/error.html', {'message': 'Author does not exist.'})







#def delete_author(request, author_id):
#    """
#    Delete an author if they are not associated with any books.
#   """
#    author = get_object_or_404(Author, pk=author_id)
#    if not author.books.exists():  # Check if the author is not linked to any books
#        author.delete()
#    return redirect('author:author_list')

def author_detail(request, author_id):
    """
    Display details of a specific author.
    """
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'authors/author_detail.html', {'author': author})

def update_author(request, author_id):
    """
    Update the details of an author.
    """
    author = get_object_or_404(Author, pk=author_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        patronymic = request.POST.get('patronymic')
        author.update(name=name, surname=surname, patronymic=patronymic)
        return redirect('author:author_detail', author_id=author_id)
    return render(request, 'authors/update_author.html', {'author': author})

