from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'bookstore.core'

    def ready(self):
        from bookstore.core.signals import signal_created_lended