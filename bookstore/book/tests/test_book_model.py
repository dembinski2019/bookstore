from django.test import TestCase
from bookstore.book.models import Book


class BookModelTestCase(TestCase):

    def setUp(self):
        self.obj = Book(
            title ="Pense em python",
            description = "Pense como um programador python",
            author = "Allen B. Downey"
            )
        
        self.obj.save()

    def test_created(self):
        self.assertTrue(Book.objects.exists())

    def test_str(self):
        self.assertEqual("Pense em python", str(self.obj))
    
    def test_available(self):
        self.assertEqual("disponivel", self.obj.status)
    
    def test_update_status_to_reserved(self):
        self.obj.reserverd_or_borrowed()
        self.assertEqual("emprestado", self.obj.status)