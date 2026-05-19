from django.urls import path
from core.views import say_hello, post_list, post_details, new_post

urlpatterns = [
    path('hello/', say_hello),
    path('posts/', post_list, name='post_list'),
    path('post/<post_id>/', post_details, name='post_details'),
    path('new/post/', new_post, name='new_post'),
]