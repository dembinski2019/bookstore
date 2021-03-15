from django.db import models

class Client(models.Model):
    name = models.CharField("Nome", max_length=200)
    email = models.EmailField("Email")
    cpf = models.CharField("CPF", max_length=11)
    phone = models.CharField("Telefone", max_length=11)
    address = models.CharField("Endereço", max_length=255)
    active = models.BooleanField("Ativo", default=True)
    created_at = models.DateTimeField("Criado em", auto_now_add=True)

    def __str__(self):
        return self.name
        