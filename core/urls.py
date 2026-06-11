from django.urls import path
from core.views import say_hello, post_list, post_details, new_post, edit_post, delete_post, home

urlpatterns = [
    path('hello/', say_hello),
    path('posts/', post_list, name='post_list'),
    path('post/<post_id>/', post_details, name='post_details'),
    path('new/post/', new_post, name='new_post'),
    path('edit/post/<post_id>/', edit_post, name='edit_post'),
    path('delete/post/<post_id>/', delete_post, name='delete_post'),
    path('', home, name='home'),
]