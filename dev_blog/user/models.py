from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    full_name = models.CharField(max_length=255)


# Definir el modelo de Profile
class Profile(models.Model):
    """
    Esta clase representa el perfil de usuario en la aplicación web.

    Atributos:
        - photo (ImageField): La foto de perfil del usuario (opcional).
        - profession (str): La profesión del usuario (opcional), limitada a 50 caracteres.
        - about (str): Información adicional sobre el usuario (opcional).
        - birthday (DateField): La fecha de nacimiento del usuario (opcional).
        - twitter (URLField): Enlace al perfil de Twitter del usuario (opcional), limitado a 50 caracteres.
        - linkedin (URLField): Enlace al perfil de LinkedIn del usuario (opcional), limitado a 50 caracteres.
        - facebook (URLField): Enlace al perfil de Facebook del usuario (opcional), limitado a 50 caracteres.
        - user (OneToOneField): Una clave foránea que vincula el perfil con un usuario.

    Notas:
        - Los campos marcados como "opcional" pueden estar en blanco o nulos.
        - La relación con el usuario es uno a uno (OneToOneField), lo que significa que cada perfil está asociado con un usuario.

    """

    # Campo de la foto de perfil del usuario (opcional)
    photo = models.ImageField(blank=True, null=True)
    # Campo de la profesión del usuario (opcional), limitada a 50 caracteres
    profession = models.CharField(max_length=50, null=True)
    # Campo de información adicional sobre el usuario (opcional)
    about = models.TextField(null=True)
    # Campo de fecha de nacimiento del usuario (opcional)
    birthday = models.DateField(null=True)
    # Campo de enlace al perfil de Twitter del usuario (opcional), limitado a 50 caracteres
    twitter = models.URLField(max_length=50, null=True)
    # Campo de enlace al perfil de LinkedIn del usuario (opcional), limitado a 50 caracteres
    linkedin = models.URLField(max_length=50, null=True)
    # Campo de enlace al perfil de Facebook del usuario (opcional), limitado a 50 caracteres
    facebook = models.URLField(max_length=50, null=True)
    # Clave foránea que vincula el perfil con un usuario (relación uno a uno)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
