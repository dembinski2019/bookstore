from django.test import TestCase
from bookstore.client.models import Client
from bookstore.book.models import Book
from bookstore.core.models import Lended
from datetime import date, timedelta

class LendedBaseTestCase(TestCase):
    def setUp(self):
        self.id_client = Client.objects.create(
            name="Everton Dembinski",
            email="everton@everton.com",
            cpf="012345678901",
            phone = "93 981296718",
            address="Rua Alguma coisa, 136",
        )
        self.id_book = Book.objects.create(
            title ="Pense em python",
            description = "Pense como um programador python",
            author = "Allen B. Downey"
        )
        self.lended = Lended(
            id_client = self.id_client, 
            id_book = self.id_book,
            date_of_lended = date.today(),
            return_estimate = date.today()+timedelta(days=3),
            price = 10
        )
        self.lended.save()


class LendedBookModelTestCase(LendedBaseTestCase):
    def test_lended_exits(self):
        self.assertTrue(Lended.objects.exists())

    def test_str(self):
        self.assertEqual(f'{self.id_client}: emprestou {self.id_book} - {date.today()}',
                        str(self.lended))
    
    def test_book_status_lended(self):
        book = Book.objects.get(pk=self.lended.pk)
        self.assertEqual("emprestado", book.status)

class LendedReturnInTheDateBookTestCase(LendedBaseTestCase):
    def setUp(self):
        super().setUp()
        self.lended.return_book()

    def test_return_book_on_the_date(self):
        expected = date.today()
        self.assertEqual(expected,self.lended.return_date)
    
    def test_return_invoice_price(self):
        expected = 10
        received = self.lended.pay_interest_rate()
        self.assertEqual(expected, received)




class LendedReturnInTheDateBookTestCase(LendedBaseTestCase):

    def setUp(self):
        super().setUp()
        self.lended = Lended(
            id_client = self.id_client, 
            id_book = self.id_book,
            date_of_lended = date.today()+timedelta(days=-4),
            return_estimate = date.today()+timedelta(days=-3),
            price = 10
        )
        self.lended.save()
        self.lended.return_book()
    
    def test_return_book_with_late(self):
        self.assert_(self.lended.return_date > self.lended.return_estimate)
    
    
    def test_return_invoice_price_3_days_of_late(self):
        expected = 10.37
        received = self.lended.pay_interest_rate()
        self.assertEqual(expected, received)
    
    def test_return_invoice_price_5_days_of_late(self):
        expected = 10.72
        self.lended.return_estimate = date.today()+timedelta(days=-5)
        received = self.lended.pay_interest_rate()
        self.assertEqual(expected, received)
        
    def test_return_invoice_price_8_days_of_late(self):
        expected = 11.23
        self.lended.return_estimate = date.today()+timedelta(days=-8)
        received = self.lended.pay_interest_rate()
        self.assertEqual(expected, received)