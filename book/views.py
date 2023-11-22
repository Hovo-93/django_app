from django.http import JsonResponse
from rest_framework import generics
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer


class BookList(generics.ListCreateAPIView):
    """
        Класс для создания и осмотра книг
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
         Класс для удаления обновления
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_update(self, serializer):
        serializer.save()
        return Response({'message': 'Book updated'}, status=200)

    def perform_destroy(self, instance):
        instance.delete()
        return Response({'message': f'{instance.id} Book deleted successfully'}, status=204)

