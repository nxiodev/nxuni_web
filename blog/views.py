from django.shortcuts import render
from blog.models import Post
from django.http import HttpResponse
from .models import *

# Create your views here.

def blog(request):
    
    posts = Post.objects.all()

    return render(request, 'blog/blog.html', {'posts': posts})

def post(request, blog_id):
    blogger = Post.objects.get(pk=blog_id)
    return HttpResponse(f'''<p style="background-color:red;text-align:center">estas viendo el blog {blog_id} {blogger}<p>
                            <div style="background-color:aqua;height:90vh;">Contenido del blog</div>
    ''')