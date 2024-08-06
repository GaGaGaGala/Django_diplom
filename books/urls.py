from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.book_detail, name='book_detail'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contact, name='contacts'),
]
