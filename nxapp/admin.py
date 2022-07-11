from django.contrib import admin
from .models import Newsletter
# Register your models here.
class NewsLetteradmin(admin.ModelAdmin):
    list_display = ('email','date')

admin.site.register(Newsletter,NewsLetteradmin)