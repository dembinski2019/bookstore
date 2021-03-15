from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

routers = DefaultRouter()
routers.register("", views.BookViewSet)

urlpatterns = [
    path("", include(routers.urls)),
    path("<int:pk>/reserve/", views.reserve_book)
]