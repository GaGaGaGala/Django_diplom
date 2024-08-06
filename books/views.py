from django.shortcuts import render, get_object_or_404
from .models import Book

def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'books/book_detail.html', {'book': book})

def about(request):
    return render(request, 'books/about.html')

def contact(request):
    if request.method == 'POST':
        # Получите данные формы из POST-запроса
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Вы можете обработать сообщение, например, сохранить его в базе данных
        # или отправить по электронной почте. Здесь мы просто выводим его на экран.
        print(f'Сообщение от {name} ({email}): {message}')

        # Отправьте ответ клиенту
        return render(request, 'books/contacts.html', {'success': True})
    return render(request, 'books/contacts.html')
