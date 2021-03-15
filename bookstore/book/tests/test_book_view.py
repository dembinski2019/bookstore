from django.test import TestCase
from bookstore.book.models import Book

class TestBookGet(TestCase):
    def setUp(self):
        self.response = self.client.get("/books/")

    def test_get(self):
        self.assertEqual(self.response.status_code,200)

    def test_get_return_a_list(self):
        self.assertEqual(self.response.json(), [])


class TestBookPostValid(TestCase):
    def setUp(self):
        self.data = dict(
            title ="Pense em python",
            description = "Pense como um programador python",
            author = "Allen B. Downey"    
        )
        self.response = self.client.post("/books/", data=self.data)

    def test_post_sucess(self):
        self.assertEqual(self.response.status_code, 201)
    
    def test_post_are_db(self):
        self.assertEqual(self.response.json()['title'], self.data['title'] )
    
    def test_post_exists_in_db(self):
        self.assertEqual(Book.objects.count(), 1)

class TestBookPostInvalid(TestCase):
    def setUp(self):
        self.data = dict(
            description = "Pense como um programador python",
            author = "Allen B. Downey"    
        )
        self.response = self.client.post("/books/", data=self.data)
    
    def test_post_missing_title(self):
        self.assertEqual(self.response.status_code,400)
    
    def test_post_missing_title(self):
        self.assertEqual(self.response.json()['title'],
                        ['This field is required.'])


class BookDelete(TestCase):
    def setUp(self):
        data = dict(
            title ="Pense em python",
            description = "Pense como um programador python",
            author = "Allen B. Downey"    
        )
        self.client.post("/books/", data=data)
        self.response = self.client.delete("/books/1/")
    
    def test_delete_sucess(self):
        self.assertEqual(self.response.status_code, 204)

    def test_not_exists(self):
        self.assertEqual(Book.objects.count(),0)