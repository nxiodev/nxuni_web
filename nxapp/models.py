from django.db import models

# Create your models here.
class Newsletter(models.Model):
    
    email = models.EmailField(max_length=30, verbose_name="user email",unique=False)

    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.email