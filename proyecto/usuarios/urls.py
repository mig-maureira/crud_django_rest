from django.urls import path
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views
from .views import UserViewSet, registro
from . import views

router = DefaultRouter()
router.register(r"user", UserViewSet)

urlpatterns = router.urls + [
    path("registro/", views.registro, name="registro"),
]
