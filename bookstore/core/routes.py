from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views


routers = DefaultRouter()
routers.register("emprestar",views.BookLendedApiView)
urlpatterns = [
    path("", include(routers.urls)),
]

