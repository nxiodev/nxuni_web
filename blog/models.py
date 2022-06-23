from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4


class Categoria(models.Model):

    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=80, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.id)


class Blogger(models.Model):

    id = models.BigAutoField(primary_key=True)
    usuario = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="blogger_profile"
    )
    image = models.ImageField(upload_to="bloggers_img", null=True, default=None)
    nombre = models.CharField(max_length=80)
    apellidos = models.CharField(max_length=80)
    correo_electronico = models.EmailField(unique=True)


    def __str__(self):
        return str(self.usuario)


class Post(models.Model):

    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    # image = models.ImageField(upload_to="imagblogs", null=True, default=None)
    blogger = models.ForeignKey(
        Blogger, default=None, null=True, on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    categorias = models.ManyToManyField(Categoria)

    @property
    def get_main_category(self):
        main_category = self.categorias[0]
        return main_category
    # , on_delete=models.CASCADE)

    def __str__(self):
        return self.title
