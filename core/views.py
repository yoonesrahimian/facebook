from django.shortcuts import render
from core.models import Post

# Create your views here.

def say_hello (request):
    # context = {'name':'laptop', 'brand':'asus', 'price':1000000}
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'index.html', context=context)

def post_list(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'index.html', context=context)

def post_details(request, post_id):
    post = Post.objects.filter(id=post_id).first()
    context = {'post':post}
    return render(request, 'post_details.html', context=context)

def new_post(request):
    return render(request, 'new_post.html')