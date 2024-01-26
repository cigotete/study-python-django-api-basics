from rest_framework import serializers
from .models import Book, Author

class BookSerializer(serializers.ModelSerializer):
  class Meta:
    fields = (
    "name",
    "authors",
    )
    model = Book

class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    fields = (
    "name",
    "title",
    "birth_date",
    )
    model = Author