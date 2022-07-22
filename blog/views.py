from django.shortcuts import render
from django.http import HttpResponse

from .models import Post, Categoria

# Create your views here.

def blog(request):
    posts = Post.objects.all().prefetch_related("categorias")
    categorias = Categoria.objects.all()

    for p in posts:
        print(p.image)

    return render(request, 'blog/blog.html', {
        'posts': posts,
        'categorias': categorias,
    })


def post_view(request, blog_id):
    blogger = Post.objects.get(pk=blog_id)
    return render(request,'blog/post.html',{
        'blog_id' : blog_id
    })


# def count_posts(request, )