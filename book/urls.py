from django.urls import path
from .views import BookList, BookDetailView

urlpatterns = [
    path('book/', BookList.as_view(), name='book-l-c'),  # Для списка книг
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-d-u'),  # Для детальной информации о книге по ее ID
]