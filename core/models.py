from django.db import models

# Create your models here.

class CountryChoices(models.TextChoices):
    iran = ('iran', 'ایران')
    usa = ('usa', 'آمریکا')

class SubjectChoices(models.TextChoices):
    sport = ('1', 'ورزشی')
    social = ('2','شبکه اجتماعی')

class User(models.Model):
    username = models.CharField('نام کاربری', max_length=60)
    password = models.CharField('رمز عبور', max_length=32)
    birthdate = models.DateField('تاریخ تولد')
    email = models.EmailField('ایمیل')
    phone = models.CharField('شماره تلفن')
    profile = models.ImageField('پروفایل', upload_to='profile.pictures', default='avatar.jpg')
    country = models.CharField('کشور', max_length=60, choices=CountryChoices, default=CountryChoices.iran)
    is_private = models.BooleanField('آیا خصوصی باشد', default=False)

    def __str__(self):
        return f'{self.username}'
    
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربر'

class Post(models.Model):
    title = models.CharField('عنوان', max_length=60)
    content = models.TextField('محتوا')
    created_at = models.DateTimeField('زمان ساخت', auto_now_add=True)
    last_update = models.DateTimeField('آخرین ویرایش', auto_now=True)
    user = models.ForeignKey(to='User',verbose_name='کاربر', on_delete=models.CASCADE)
    visible = models.BooleanField('قابل مشاهده', default=False)
    is_deleted = models.BooleanField('آیا پاک شده', default=False)
    subject = models.CharField('موضوع', max_length=1, choices=SubjectChoices, default=SubjectChoices.sport)
    
    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست'
