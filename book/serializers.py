from rest_framework import serializers
from .models import Book
from author.serializers import AuthorSerializer
class BookSerializer(serializers.ModelSerializer):
    author_id=serializers.IntegerField(write_only=True)
    author=AuthorSerializer(read_only=True)


  
    class Meta:
        model = Book
        fields = ['id','title','rating','author','author_id']
        read_only_fields = ['id']