from django.test import TestCase
from bookstore.book.models import Book
from bookstore.client.models import Client
from bookstore.core.models import Lended
from datetime import date, timedelta
from rest_framework import exceptions

class TestClientLendsBookSucess(TestCase):
    
    def setUp(self):
        client = dict(
            name = "Everton Dembinski",
            email = "everton@everton.com",
            cpf = "12345678901",
            phone = "93981296718",
            address = "Rua Alguma coisa, 136",
        )
        self.client.post("/client/", data=client)
        book = dict(
            title ="Pense em python",
            description = "Pense como um programador python",
            author = "Allen B. Downey"    
        )
        self.client.post("/books/", data=book)
        data = dict(
            id_client = 1 ,
            id_book = 1,
            return_estimate = date.today()+timedelta(days=3),
            price = 30
            
        )
        self.response = self.client.post("/book/emprestar/", data=data) 
    
    def test_post(self):
        self.assertEqual(self.response.status_code, 201)

    def test_lended_exists(self):
        received = Lended.objects.all().count()
        self.assertEqual(received, 1)
    
    def test_lended_not_permited_book_lended(self):
        data = dict(
            id_client = 1 ,
            id_book = 1,
            return_estimate = date.today()+timedelta(days=3),
            price = 30
        )
        self.resp = self.client.post("/book/emprestar/", data=data)
        self.assertEqual(self.resp.status_code, 400)
