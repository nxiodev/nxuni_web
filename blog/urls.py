from . import views
from django.urls import path

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path("blog/<int:blog_id>/",views.post_view, name='post')
]