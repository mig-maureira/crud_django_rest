from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.inicio, name="home"),
    path("crear/", views.crear_libro, name="crear_libro"),
    path("editar/<int:pk>/", views.editar_libro, name="editar_libro"),
    path("eliminar/<int:pk>/", views.eliminar_libro, name="eliminar_libro"),
    # Auth (frontend)
    # path("registro/", registro, name="registro"),
    path(
        "login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    # path("perfil/", editar_perfil, name="perfil"),
    path("libro/<int:pk>/", views.detalle_libro, name="detalle_libro"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
