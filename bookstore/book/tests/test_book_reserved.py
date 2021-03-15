from django.test import TestCase
from bookstore.book.models import Book


class BookReservedSucessTestCase(TestCase):
    def setUp(self):
        data = dict(
            title ="Pense em python",
            description = "Pense como um programador python",
            author = "Allen B. Downey"    
        )
        self.client.post("/books/", data=data)
        self.response = self.client.post("/books/1/reserve/")

    def test_post_return_status_code_200(self):
        self.assertEqual(self.response.status_code,200)

    def test_reserved_sucess(self):
        result = Book.objects.get(id=1)
        self.assertEqual("emprestado", result.status)


class BookReservedFailTestCase(TestCase):
    def setUp(self):
        self.response = self.client.post("/books/1/reserve/")
    
    def test_reverved_not_valid_return_404(self):
        self.assertEqual(self.response.status_code,404)