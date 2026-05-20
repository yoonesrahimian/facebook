from django.shortcuts import render, HttpResponse
from core.models import Post, User
from core.forms import PostForm

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
    form = PostForm()
    # if request.method == 'POST':
    #     title = request.POST.get('title')
    #     content = request.POST.get('content')
    #     user = request.POST.get('user')
    #     user = User.objects.filter(username=user).first()
    #     subject = request.POST.get('subject')
    #     new_post = Post.objects.create(title=title, content=content, user=user, subject=subject)
    #     return HttpResponse(str(new_post))
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            user = User.objects.filter(username=form.cleaned_data.get('user')).first()
            subject = form.cleaned_data.get('subject')
            new_post = Post.objects.create(title=title, content=content, user=user, subject=subject)
            return HttpResponse(str(new_post))

    return render(request, 'new_post.html', context={'form':form})