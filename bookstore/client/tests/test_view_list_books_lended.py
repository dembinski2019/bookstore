from django.test import TestCase
from datetime import date, timedelta

class TestViewListBooksLendedBase(TestCase):
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
        self.client.post("/books/", data=book)
        data = dict(
            id_client = 1 ,
            id_book = 1,
            return_estimate = date.today()+timedelta(days=3),
            price = 30
        )
        self.client.post("/book/emprestar/", data=data) 


class TestViewListBooksLended(TestViewListBooksLendedBase):
    def setUp(self):
        super().setUp()
        self.response = self.client.get("/client/1/books/")

    def test_get(self):
        self.assertEqual(self.response.status_code,200)
    
    def test_get_return_list(self):
        self.assertIsInstance(self.response.json(),list)
    
    def test_client_name(self):
        self.assertIn("Everton Dembinski", self.response.json()[0]['client'])