# from _typeshed import ReadOnlyBuffer
from django.contrib import admin
from .models import *
# Register your models here.

class bloggerAdmin(admin.ModelAdmin):
    readonly_fields = ('usuario', 'correo_electronico',)

class blogAdmin(admin.ModelAdmin):
    readonly_fields = ('blogger','created', 'updated',)

class categoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('categoria_id','nombre', 'created',)

admin.site.register(Post)
admin.site.register(Categoria)
admin.site.register(Blogger)
