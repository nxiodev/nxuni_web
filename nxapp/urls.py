from django.contrib import admin
from django.urls import path, include
from nxapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contacto', views.contacto, name='contacto'),
    path('home', views.home, name='home'),
    path('consultoria', views.servicios, name='servicios'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)