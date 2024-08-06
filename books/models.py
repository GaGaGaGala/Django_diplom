from django.db import models

class Book(models.Model):
    # id = models.IntegerField(verbose_name="ID книги")
    title = models.CharField(max_length=200, verbose_name="Название")
    author = models.CharField(max_length=100, verbose_name="Автор")
    publication_year = models.IntegerField(verbose_name="Год публикации")
    description = models.TextField(verbose_name="Описание")
    cover_image = models.URLField(verbose_name="Фотография")

    def __str__(self):
        return self.title
