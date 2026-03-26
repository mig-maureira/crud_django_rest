# python manage.py shell

from libreria.models import Libro

Libro.objects.create(
    titulo="Don Quijote de la Mancha",
    autor="Miguel de Cervantes",
    anio_publicacion=1605,
    disponible=True,
)

Libro.objects.create(
    titulo="Cien años de soledad",
    autor="Gabriel García Márquez",
    anio_publicacion=1967,
    disponible=True,
)

Libro.objects.create(
    titulo="La sombra del viento",
    autor="Carlos Ruiz Zafón",
    anio_publicacion=2001,
    disponible=True,
)

Libro.objects.create(
    titulo="El amor en los tiempos del cólera",
    autor="Gabriel García Márquez",
    anio_publicacion=1985,
    disponible=True,
)

Libro.objects.create(
    titulo="La casa de los espíritus",
    autor="Isabel Allende",
    anio_publicacion=1982,
    disponible=True,
)

Libro.objects.create(
    titulo="Rayuela", autor="Julio Cortázar", anio_publicacion=1963, disponible=True
)

Libro.objects.create(
    titulo="Pedro Páramo", autor="Juan Rulfo", anio_publicacion=1955, disponible=True
)

Libro.objects.create(
    titulo="El túnel", autor="Ernesto Sabato", anio_publicacion=1948, disponible=True
)

Libro.objects.create(
    titulo="Ficciones",
    autor="Jorge Luis Borges",
    anio_publicacion=1944,
    disponible=True,
)

Libro.objects.create(
    titulo="Crónica de una muerte anunciada",
    autor="Gabriel García Márquez",
    anio_publicacion=1981,
    disponible=True,
)

Libro.objects.create(
    titulo="El principito",
    autor="Antoine de Saint-Exupéry",
    anio_publicacion=1943,
    disponible=True,
)

Libro.objects.create(
    titulo="1984", autor="George Orwell", anio_publicacion=1949, disponible=True
)

Libro.objects.create(
    titulo="Rebelión en la granja",
    autor="George Orwell",
    anio_publicacion=1945,
    disponible=True,
)

Libro.objects.create(
    titulo="Orgullo y prejuicio",
    autor="Jane Austen",
    anio_publicacion=1813,
    disponible=True,
)

Libro.objects.create(
    titulo="Matar a un ruiseñor",
    autor="Harper Lee",
    anio_publicacion=1960,
    disponible=True,
)

Libro.objects.create(
    titulo="El gran Gatsby",
    autor="F. Scott Fitzgerald",
    anio_publicacion=1925,
    disponible=True,
)

Libro.objects.create(
    titulo="Drácula", autor="Bram Stoker", anio_publicacion=1897, disponible=True
)

Libro.objects.create(
    titulo="Frankenstein", autor="Mary Shelley", anio_publicacion=1818, disponible=True
)

Libro.objects.create(
    titulo="El señor de los anillos",
    autor="J. R. R. Tolkien",
    anio_publicacion=1954,
    disponible=True,
)

Libro.objects.create(
    titulo="El nombre de la rosa",
    autor="Umberto Eco",
    anio_publicacion=1980,
    disponible=True,
)

Libro.objects.create(
    titulo="El Hobbit", autor="J. R. R. Tolkien", anio_publicacion=1937, disponible=True
)

Libro.objects.all()
