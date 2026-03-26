# crud_django_rest

# Proyecto Librería - Django

Este es un proyecto web desarrollado con Django que permite la gestión de un catálogo de libros y el registro de usuarios, incluyendo endpoints de una API REST.

## 🚀 Tecnologías Utilizadas

- **Backend:** Python, Django 6.0.3
- **API:** Django REST Framework (DRF) 3.17.1
- **Base de Datos:** PostgreSQL (conector psycopg2 2.9.11)
- **Procesamiento de Imágenes:** Pillow 12.1.1
- **Frontend:** Plantillas de Django con integración de clases de Bootstrap

## ⚙️ Requisitos Previos

Para ejecutar este proyecto de forma local, necesitas tener instalado:

- Python 3.x
- PostgreSQL corriendo localmente en el puerto `5433` con el usuario `postgres` y la contraseña `admin1234`.

## 🛠️ Instalación y Configuración Local

1.  **Clonar el repositorio:**

    ```bash
    git clone https://github.com/mig-maureira/crud_django_rest
    cd crud_django_rest
    ```

2.  **Crear y activar un entorno virtual:**

    ```bash
    python -m venv venv

    # En Windows:
    venv\Scripts\activate
    # En macOS/Linux:
    source venv/bin/activate
    ```

3.  **Instalar dependencias:**
    Utiliza el archivo de requerimientos para instalar todas las librerías necesarias con sus versiones exactas:

    ```bash
    pip install -r requeriments.txt
    ```

    _(Nota: El archivo está nombrado como `requeriments.txt`, asegúrate de usar ese nombre en el comando)._

4.  **Configurar la base de datos:**
    Abre tu gestor de PostgreSQL (como pgAdmin o la terminal) y crea una base de datos llamada `libreria`.

5.  **Aplicar migraciones:**
    Genera y aplica las tablas necesarias en la base de datos:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6.  **Ejecutar el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```
    El proyecto estará disponible en `http://localhost:8000/`.

## 📂 Estructura Principal

- **Aplicación `libreria`**: Gestiona el catálogo de libros. Contiene el modelo `Libro` (que incluye soporte para subir imágenes de portada) y formularios estilizados para la interfaz de usuario.
- **Aplicación `usuarios`**: Maneja el registro y autenticación. Incluye configuraciones de DRF para serializar usuarios y encriptar contraseñas de manera segura.

## 🔗 Rutas y API

El proyecto expone las siguientes rutas principales:

- `/registro/`: Vista tradicional para el registro de nuevos usuarios en la plataforma.
- `/user/`: Endpoint principal de la API REST para interactuar con el modelo de usuarios (provisto por el router de DRF).

## 🖼️ Manejo de Archivos Multimedia

Los archivos subidos por los usuarios, como las imágenes de portada de los libros, se guardan en el directorio local `media/portadas/` y son servidos en la ruta URL `/media/`.
