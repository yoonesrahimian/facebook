from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = models.CharField('شماره تلفن', max_length=11)
    addres = models.CharField('آدرس', max_length=256)
    city = models.CharField('شهر', max_length=256)
    profile_picture = models.ImageField('پروفایل', upload_to='profile_pictures', default='avatar.png')

    def __str__(self):
        return f'{self.username}'
    
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربر'
