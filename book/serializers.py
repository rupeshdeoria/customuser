#from django.core import serializers
from rest_framework import serializers
from book.models import Book
class BookSerializer(serializers.ModelSerializer):
    """
    Serializing all the Authors
    """
    class Meta:
        model = Book
        fields = ('id','book_name', 'book_title')