from django.test import TestCase
from bookstore.client.models import Client


class TestClientGet(TestCase):
    def setUp(self):
        self.response = self.client.get("/client/")

    def test_get(self):
        self.assertEqual(self.response.status_code,200)

    def test_get_return_a_list(self):
        self.assertEqual(self.response.json(), [])

class TestClientPostValid(TestCase):
    def setUp(self):
        self.data = dict(
            name = "Everton Dembinski",
            email = "everton@everton.com",
            cpf = "12345678901",
            phone = "93981296718",
            address = "Rua Alguma coisa, 136",
        )
        self.response = self.client.post("/client/", data=self.data)

    def test_post_sucess(self):
        self.assertEqual(self.response.status_code, 201)
    
    def test_post_are_db(self):
        self.assertEqual(self.response.json()['name'], self.data['name'] )

    def test_post_exists_in_db(self):
        self.assertEqual(Client.objects.count(), 1)

class TestClientPostInvalid(TestCase):
    def setUp(self):
        self.data = dict(
            email = "everton@everton.com",
            cpf = "12345678901",
            phone = "93981296718",
            address = "Rua Alguma coisa, 136",
        )
        self.response = self.client.post("/client/", data=self.data)
    
    def test_post_missing_error(self):
        self.assertEqual(self.response.status_code,400)
    
    def test_post_missing_name(self):
        self.assertEqual(self.response.json()['name'],
                        ['This field is required.'])

class TestClientDelete(TestCase):
    def setUp(self):
        data = dict(
            name = "Everton Dembinski",
            email = "everton@everton.com",
            cpf = "12345678901",
            phone = "93981296718",
            address = "Rua Alguma coisa, 136",
        )
        self.client.post("/client/", data=data)
        self.response = self.client.delete("/client/1/")
    
    def test_delete_sucess(self):
        self.assertEqual(self.response.status_code, 204)
    
    def test_not_exists(self):
        self.assertEqual(Client.objects.count(),0)

# class TestClientLendsBookSucess(TestCase):
    
        
#     def test_get(self):
#         self.assertEqual(self.response.status_code, 200)
        