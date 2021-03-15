from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics
from .models import Client
from .serializers import ClientSerializer
from bookstore.book.serializers import BookSerializer
from bookstore.core.serializers import LendedSerializerBooks


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ListBooksLendedClient(generics.ListAPIView):
    serializer_class = LendedSerializerBooks
    
    def get_queryset(self):
        client = get_object_or_404(Client, pk=self.kwargs['id'])
        return client.my_lended.all()


    