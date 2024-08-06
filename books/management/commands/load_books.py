import json
from django.core.management.base import BaseCommand
from books.models import Book

class Command(BaseCommand):
    help = 'Load books from books.json'

    def handle(self, *args, **kwargs):
        with open('books.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for item in data:
                Book.objects.create(
                    # id=item['id книги'],
                    title=item['название'],
                    author=item['автор'],
                    publication_year=item['год публикации'],
                    description=item['описание'],
                    cover_image=item['фотография']
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded books'))
