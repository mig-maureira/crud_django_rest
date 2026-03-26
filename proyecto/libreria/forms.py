from django import forms
from .models import Libro


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = [
            "titulo",
            "autor",
            "anio_publicacion",
            "portada",
            "disponible",
            "genero",
        ]

        # estilos de Bootstrap para cada campo
        widgets = {
            "titulo": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej: El Quijote de la Mancha",
                }
            ),
            "autor": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre del autor"}
            ),
            "anio_publicacion": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Año (Ej: 1605)"}
            ),
            "portada": forms.FileInput(attrs={"class": "form-control"}),
            "disponible": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "genero": forms.TextInput(attrs={"class": "form-control"}),
        }

        labels = {
            "titulo": "Título del Libro",
            "anio_publicacion": "Año de Publicación",
            "portada": "Imagen de Portada",
        }
