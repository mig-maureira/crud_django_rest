from rest_framework import viewsets
from .serializers import UserSerializer
from django.contrib.auth.models import User
import requests
from django.shortcuts import render, redirect

# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserChangeForm


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def registro(request):
    if request.method == "POST":
        data = {
            "username": request.POST.get("username"),
            "email": request.POST.get("email"),
            "password": request.POST.get("password"),
        }

        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return redirect("login")
        else:
            print(serializer.errors)  # 👈 DEBUG

    return render(request, "registro.html")


# def registro(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("login")
#     else:
#         form = UserCreationForm()

#     return render(request, "registro.html", {"form": form})


# @login_required
# def editar_perfil(request):
#     if request.method == "POST":
#         form = UserChangeForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect("home")
#     else:
#         form = UserChangeForm(instance=request.user)

#     return render(request, "editar_perfil.html", {"form": form})
