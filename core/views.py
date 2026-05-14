from django.shortcuts import render
from core.models import Post

# Create your views here.

def say_hello (request):
    # context = {'name':'laptop', 'brand':'asus', 'price':1000000}
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'index.html', context=context)