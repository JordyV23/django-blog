from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
# Definir el modelo de Category
class Category(models.Model):
    """
       Esta clase representa una categoría en la aplicación web.

       Atributos:
           - name (str): El nombre de la categoría.
           - image (ImageField): La imagen asociada a la categoría.
           - slug (SlugField): La cadena amigable para URL única de la categoría.
           - featured (bool): Indica si la categoría está destacada.
           - created (DateTimeField): La fecha y hora de creación de la categoría.
           - updated (DateTimeField): La fecha y hora de actualización de la categoría.
           - status (bool): Indica el estado de la categoría (activo o inactivo).

       Métodos:
           - __str__(): Devuelve una representación en cadena del objeto de categoría.

       Meta:
           - verbose_name (str): El nombre en singular para el modelo en el panel de administración.
           - verbose_name_plural (str): El nombre en plural para el modelo en el panel de administración.
       """

    # Campo de nombre de la categoría, se limita a 20 caracteres
    name = models.CharField(max_length=20)
    # Campo de imagen de la categoría, no puede estar en blanco (blank=False) y no puede ser nulo (null=False)
    image = models.ImageField(blank=False, null=False)
    # Campo de slug (cadena amigable para URL) único para cada categoría, limitado a 40 caracteres
    slug = models.SlugField(unique=True, max_length=40)
    # Campo booleano que indica si la categoría está destacada, con un valor predeterminado de False
    featured = models.BooleanField(default=False)
    # Campo de fecha y hora de creación de la categoría, se establece automáticamente cuando se crea una categoría
    created = models.DateTimeField(auto_now_add=True)
    # Campo de fecha y hora de actualización de la categoría
    # se actualiza automáticamente cada vez que se modifica la categoría
    updated = models.DateTimeField(auto_now=True)
    # Campo booleano que indica el estado de la categoría, con un valor predeterminado de True
    status = models.BooleanField(default=True)

    def __str__(self):
        # Representación en cadena de la categoría, que es su nombre
        return self.name

    class Meta:
        # Configuración de metadatos para el modelo
        verbose_name = 'Category'  # Nombre en singular para el modelo en el panel de administración de Django
        verbose_name_plural = 'Categories'  # Nombre en plural para el modelo en el panel de administración de Django


# Definir el modelo de Article
class Article(models.Model):
    """
    Esta clase representa un artículo en la aplicación web.

    Atributos:
        - title (str): El título del artículo.
        - introduction (str): La introducción del artículo.
        - slug (SlugField): La cadena amigable para URL única del artículo.
        - image (ImageField): La imagen asociada al artículo.
        - body (str): El cuerpo del artículo.
        - user_id (ForeignKey): Una clave foránea que vincula el artículo con un usuario.
        - categories (ManyToManyField): Relación many-to-many con las categorías a las que pertenece el artículo.
        - created (DateTimeField): La fecha y hora de creación del artículo.
        - updated (DateTimeField): La fecha y hora de actualización del artículo.
        - status (bool): Indica el estado del artículo (activo o inactivo).

    Métodos:
        - __str__(): Devuelve una representación en cadena del objeto de artículo.

    Meta:
        - verbose_name (str): El nombre en singular para el modelo en el panel de administración.
        - verbose_name_plural (str): El nombre en plural para el modelo en el panel de administración.
    """

    # Campo de título del artículo, se limita a 255 caracteres
    title = models.CharField(max_length=255)
    # Campo de introducción del artículo, se limita a 255 caracteres
    introduction = models.CharField(max_length=255)
    # Campo de slug (cadena amigable para URL) único para cada artículo, limitado a 255 caracteres
    slug = models.SlugField(unique=True, max_length=255)
    # Campo de imagen del artículo
    image = models.ImageField()
    # Campo de cuerpo del artículo
    body = models.TextField()
    # Clave foránea que vincula el artículo con un usuario
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # Relación many-to-many con las categorías a las que pertenece el artículo
    categories = models.ManyToManyField(Category)
    # Campo de fecha y hora de creación del artículo, se establece automáticamente cuando se crea un artículo
    created = models.DateTimeField(auto_now_add=True)
    # Campo de fecha y hora de actualización del artículo.
    # Se actualiza automáticamente cada vez que se modifica el artículo
    updated = models.DateTimeField(auto_now=True)
    # Campo booleano que indica el estado del artículo, con un valor predeterminado de True
    status = models.BooleanField(default=True)

    def __str__(self):
        # Representación en cadena del artículo, que es su título
        return self.title

    class Meta:
        # Configuración de metadatos para el modelo
        verbose_name = 'Article'  # Nombre en singular para el modelo en el panel de administración de Django
        verbose_name_plural = 'Articles'  # Nombre en plural para el modelo en el panel de administración de Django


# Definir el modelo de Rating
class Rating(models.Model):
    """
    Esta clase representa una calificación de un artículo en la aplicación web.

    Atributos:
        - valued (float): El valor de la calificación.
        - description (str): Una descripción opcional de la calificación.
        - article_id (ForeignKey): Una clave foránea que vincula la calificación con un artículo.
        - user_id (ForeignKey): Una clave foránea que vincula la calificación con un usuario.
        - created (DateTimeField): La fecha y hora de registro de la calificación.
        - updated (DateTimeField): La fecha y hora de actualización de la calificación.
        - status (bool): Indica el estado de la calificación (activo o inactivo).

    Métodos:
        - __str__(): Devuelve una representación en cadena del objeto de calificación.

    Meta:
        - verbose_name (str): El nombre en singular para el modelo en el panel de administración.
        - verbose_name_plural (str): El nombre en plural para el modelo en el panel de administración.
    """

    # Campo del valor de la calificación
    valued = models.FloatField()
    # Campo de descripción opcional de la calificación, se limita a 255 caracteres
    description = models.CharField(max_length=255)
    # Clave foránea que vincula la calificación con un artículo
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    # Clave foránea que vincula la calificación con un usuario
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # Campo de fecha y hora de registro de la calificación, se establece automáticamente cuando se crea una calificación
    created = models.DateTimeField(auto_now_add=True)
    # Campo de fecha y hora de actualización de la calificación.
    # Se actualiza automáticamente cada vez que se modifica la calificación
    updated = models.DateTimeField(auto_now=True)
    # Campo booleano que indica el estado de la calificación, con un valor predeterminado de True
    status = models.BooleanField(default=True)

    def __str__(self):
        # Representación en cadena de la calificación, que es el nombre de usuario del usuario que la hizo
        return self.user_id.username

    class Meta:
        # Configuración de metadatos para el modelo
        verbose_name = 'Rating'  # Nombre en singular para el modelo en el panel de administración de Django
        verbose_name_plural = 'Ratings'  # Nombre en plural para el modelo en el panel de administración de Django
