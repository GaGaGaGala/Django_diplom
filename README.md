python -m pip install -r requirements.txt
[Flask] python app.py
[FastAPI] python -m uvicorn app.main:app
[Django] python manage.py runserver

```
django_book/
├── django_book/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── books/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── serializers.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── templates/
│   │   ├── about.html
│   │   ├── book_detail.html
│   │   ├── contacts.html
│   │   └── index.html
│   └── management/
│       └── commands/
│           ├── __init__.py
│           └── load_books.py
│
├── books.json
├── db.sqlite3
├── manage.py
└── requirements.txt
```

#### Автор: Галина
#### Дата: 30.07.2024

quadd4rv1n7