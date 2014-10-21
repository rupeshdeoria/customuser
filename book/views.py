from django.shortcuts import render

# Create your views here.
from book.serializers import BookSerializer
from rest_framework import generics
from book.models import Book

class BookView(generics.ListAPIView):
    """
    Returns a list of all authors.
    """
    model = Book
    serializer_class = BookSerializer
