from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

# List view (used for /books/)
class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# ViewSet (used for /books_all/ CRUD)
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
