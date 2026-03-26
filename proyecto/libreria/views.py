from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Libro
from .forms import LibroForm


def inicio(request):
    libros = Libro.objects.all()

    return render(request, "home.html", {"libros": libros})


@login_required
def crear_libro(request):
    if request.method == "POST":
        form = LibroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = LibroForm()

    return render(request, "libros/crear_libro.html", {"form": form})


@login_required
def editar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)

    if request.method == "POST":

        form = LibroForm(request.POST, request.FILES, instance=libro)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = LibroForm(instance=libro)

    return render(request, "libros/editar_libro.html", {"form": form})


@login_required
def eliminar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)

    if request.method == "POST":
        libro.delete()
        return redirect("home")

    return render(request, "libros/eliminar_libro.html", {"libro": libro})


def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "registro.html", {"form": form})


def detalle_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, "libros/detalle_libro.html", {"libro": libro})
