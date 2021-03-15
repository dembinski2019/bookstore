from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

routers = DefaultRouter()
routers.register("", views.ClientViewSet)


urlpatterns = [
    path("", include(routers.urls)),
    path("<int:id>/books/", views.ListBooksLendedClient.as_view())
]
