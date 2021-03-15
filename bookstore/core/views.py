from .models import Lended
from rest_framework.generics import mixins
from rest_framework import viewsets
from .serializers import LendedSerializer
from bookstore.book.models import Book
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

class BookLendedApiView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Lended.objects.all()
    serializer_class = LendedSerializer

    def create(self, request, *args, **kwargs):
        book_id = request.data['id_book']
        book = get_object_or_404(Book, pk=book_id)
        if book.status == "emprestado":
            return Response(data={"msg": "This book is not available"},status=status.HTTP_400_BAD_REQUEST)
        return super().create(request)


