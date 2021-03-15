from rest_framework import serializers
from .models import Lended
from bookstore.book.models import Book
from bookstore.book.serializers import BookSerializer
from bookstore.client.serializers import ClientSerializer
from bookstore.client.models import Client

class LendedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lended
        fields = ["id_book","id_client","price","return_estimate"]
    

class LendedSerializerBooks(serializers.ModelSerializer):
    book = BookSerializer(read_only=True,source='id_book')
    client = serializers.CharField(source="id_client")
    class Meta:
        model = Lended
        fields = ["client",'book']

