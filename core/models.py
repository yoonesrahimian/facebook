from django.db import models
from django.contrib.auth.models import AbstractUser


class SubjectChoices(models.TextChoices):
    sport = ('1', 'ورزشی')
    social = ('2','شبکه اجتماعی')


class Post(models.Model):
    title = models.CharField('عنوان', max_length=60)
    content = models.TextField('محتوا')
    created_at = models.DateTimeField('زمان ساخت', auto_now_add=True)
    last_update = models.DateTimeField('آخرین ویرایش', auto_now=True)
    user = models.ForeignKey(to='accounts.CustomUser',verbose_name='کاربر', on_delete=models.CASCADE)
    visible = models.BooleanField('قابل مشاهده', default=False)
    is_deleted = models.BooleanField('آیا پاک شده', default=False)
    subject = models.CharField('موضوع', max_length=1, choices=SubjectChoices, default=SubjectChoices.sport)
    
    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست'
