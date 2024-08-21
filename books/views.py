from django.shortcuts import render, get_object_or_404
from .models import Book
from django.http import HttpResponse

def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'books/book_detail.html', {'book': book})

def about(request):
    return render(request, 'books/about.html')

def contact(request):
    User = []
    if request.method == 'POST':
        # Получите данные формы из POST-запроса
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        print(f'Сообщение от {name} ({email}): {message}')
        User.append(name)
        return HttpResponse(f'Приветствуем, {name}! Спасибо за отзыв.')
        # Отправьте ответ клиенту
        #return render(request, 'books/contacts.html', {'success': True})
    return render(request, 'books/contacts.html')
