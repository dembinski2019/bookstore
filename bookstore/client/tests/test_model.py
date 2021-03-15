from django.test import TestCase
from bookstore.client.models import Client
from datetime import datetime


class ClientModelTestCase(TestCase):
    def setUp(self):
        self.obj = Client(
            name="Everton Dembinski",
            email="everton@everton.com",
            cpf="012345678901",
            phone = "93 981296718",
            address="Rua Alguma coisa, 136",
        )
        self.obj.save()

    def test_client_exists(self):
        self.assertTrue(Client.objects.exists())
    
    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)
    
    def test_is_active(self):
        self.assertTrue(self.obj.active)

    def test_str(self):
        self.assertEqual('Everton Dembinski', str(self.obj))