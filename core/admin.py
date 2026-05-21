from django.contrib import admin
from core.models import Post, CustomUser

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Post)