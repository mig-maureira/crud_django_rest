from django.db import models


class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    anio_publicacion = models.IntegerField()
    portada = models.ImageField(upload_to="portadas/", null=True, blank=True)
    disponible = models.BooleanField(default=True)
    genero = models.CharField(
        default="No especificado", max_length=50, null=True, blank=True
    )

    def __str__(self):
        return self.titulo
