from django.db import models



class Book(models.Model):

    STATUS_CHOICES = (
        ("disponivel",'Disponível'),
        ("emprestado",'Emprestado'),
    )

    title = models.CharField("Título", max_length= 200)
    description = models.TextField("Descrição")
    author = models.CharField("Autor", max_length=200)
    status = models.CharField("Situação",choices=STATUS_CHOICES, default="disponivel", max_length=30)

    
    def __str__(self):
        return self.title


    def reserverd_or_borrowed(self):
        self.status = 'emprestado'
        self.save()
        self.refresh_from_db()


