from django.shortcuts import render, redirect
from .forms import AuthorForm, BookForm, BorrowRecordForm
from .models import Author, Book, BorrowRecord
from django.core.paginator import Paginator

def add_author(request):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('author-list')
    return render(request, 'add_author.html', {'form': form})

def add_book(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('book-list')
    return render(request, 'add_book.html', {'form': form})

def add_borrow_record(request):
    form = BorrowRecordForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('borrow-list')
    return render(request, 'add_borrow.html', {'form': form})

def author_list(request):
    authors = Author.objects.all()
    paginator = Paginator(authors, 5)
    page = request.GET.get('page')
    authors = paginator.get_page(page)
    return render(request, 'author_list.html', {'authors': authors})

def book_list(request):
    books = Book.objects.all()
    paginator = Paginator(books, 5)
    page = request.GET.get('page')
    books = paginator.get_page(page)
    return render(request, 'book_list.html', {'books': books})

def borrow_list(request):
    records = BorrowRecord.objects.all()
    paginator = Paginator(records, 5)
    page = request.GET.get('page')
    records = paginator.get_page(page)
    return render(request, 'borrow_list.html', {'records': records})


# from django.shortcuts import render, redirect
# from .forms import AuthorForm, BookForm, BorrowRecordForm
# from .models import Author, Book, BorrowRecord

# # Add Author
# def add_author(request):
#     form = AuthorForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('author-list')
#     return render(request, 'add_author.html', {'form': form})

# # Add Book
# def add_book(request):
#     form = BookForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('book-list')
#     return render(request, 'add_book.html', {'form': form})

# # Add Borrow Record
# def add_borrow_record(request):
#     form = BorrowRecordForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('borrow-list')
#     return render(request, 'add_borrow.html', {'form': form})

# # Author List (No Pagination)
# def author_list(request):
#     authors = Author.objects.all()
#     return render(request, 'author_list.html', {'authors': authors})

# # Book List (No Pagination)
# def book_list(request):
#     books = Book.objects.all()
#     return render(request, 'book_list.html', {'books': books})

# # Borrow Record List (No Pagination)
# def borrow_list(request):
#     records = BorrowRecord.objects.all()
#     return render(request, 'borrow_list.html', {'records': records})
