from django.db import models
from bookstore.client.models import Client
from bookstore.book.models import Book
import math
from django.core import exceptions


def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier


def calc_fees(price_ini, fine, fees, days):
    price = 0
    price_fine = float(price_ini) + (float(price_ini) * fine)
    for day in range(days):
        price_fine += (price_fine * fees)
    price = round_up(price_fine,2)
    return price

class Lended(models.Model):
    id_client = models.ForeignKey(
        Client,on_delete=models.CASCADE, 
        related_name="my_lended",
        verbose_name="Cliente"
        )
    id_book = models.ForeignKey(
        Book, on_delete=models.CASCADE,
        related_name="lended_book",
    )
    date_of_lended = models.DateField(
        "Data do Emprestimo",
        auto_now_add=True,
        )
    return_estimate = models.DateField("Retorno Estimado")
    return_date = models.DateField("Data do retorno", null=True)
    price = models.DecimalField("Preço", max_digits=10, decimal_places=2)


    def __str__(self):
        return f"{self.id_client}: emprestou {self.id_book} - {self.date_of_lended}"
    
    def return_book(self):
        from datetime import date
        self.return_date = date.today()
        self.save()
        self.refresh_from_db()
    
    def pay_interest_rate(self):
        days = (self.return_date - self.return_estimate).days
        if days <= 0:
            return self.price
        fine = 0
        fess = 0
        if days > 0 and days <= 3:
            fine = 3/100
            fess = 0.2 /100
        elif days > 3 and days <= 5:
            fess = 0.4/100
            fine = 5/100
        else:
            fess = 0.6/100
            fine = 7/100
        return calc_fees(self.price, fine, fess,days)

    