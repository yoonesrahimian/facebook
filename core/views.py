from django.shortcuts import render, HttpResponse, redirect
from core.models import Post
from accounts.models import CustomUser
from core.forms import PostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def say_hello (request):
    # context = {'name':'laptop', 'brand':'asus', 'price':1000000}
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'core/index.html', context=context)

def post_list(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'core/index.html', context=context)

def post_details(request, post_id):
    post = Post.objects.filter(id=post_id).first()
    context = {'post':post}
    return render(request, 'core/post_details.html', context=context)

@login_required()
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
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # user = User.objects.filter(username=form.cleaned_data.get('user')).first()
            # subject = form.cleaned_data.get('subject')
            # new_post = Post.objects.create(title=title, content=content, user=user, subject=subject)
            # return HttpResponse(str(new_post))
            new_post = form.save(commit=False)
            new_post.user = request.user
            form.save()
            messages.success(request, 'پست جدید با موفقیت ثبت شد')
            return redirect('post_list')
        else:
            return messages.error(request, 'ایرادی در پر کردن فرم وجود داشت')

    return render(request, 'core/new_post.html', context={'form':form})


def edit_post(request, post_id):
    post = Post.objects.filter(id=post_id).first()
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "پست با موفقیت ویرایش شد")
            return redirect('post_details', post_id=post.id)
    return render(request, 'core/edit_post.html', context={'post':post, 'form':form})


def delete_post(request, post_id):
    Post.objects.filter(id=post_id).delete()
    messages.success(request, "پست با موفقیت حذف شد")
    return redirect('post_list')