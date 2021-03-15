from rest_framework import viewsets, status
from rest_framework.generics import mixins
from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
@api_view(["POST"])
def reserve_book(request, pk):
    if request.method == "POST":
        book = get_object_or_404(Book, pk=pk)
        book.reserverd_or_borrowed()
        return Response({"msg":"Livro reservado com sucesso"}, status=status.HTTP_200_OK) 

