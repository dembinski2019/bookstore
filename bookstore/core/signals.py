from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Lended


@receiver(post_save, sender=Lended)
def signal_created_lended(sender, instance, created,**kwargs):
    if created:
        instance.id_book.reserverd_or_borrowed()
            


    