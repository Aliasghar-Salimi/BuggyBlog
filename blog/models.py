from django.db import models
from django.utils import timezone
from extentions.utils import jalali_converter
from django.utils.html import format_html
# my managers
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')
    
class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)


# Create your models here.

class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name='children', verbose_name="زیردسته")
    title = models.CharField(max_length=200, verbose_name='عنوان دسته‌بدی')
    slug = models.SlugField(max_length=100, unique = True, verbose_name="آدرس دسته‌بندی")
    status = models.BooleanField(default=True, verbose_name='آیا نمایش داده شود؟')
    position = models.IntegerField(verbose_name='پوزیش')

    class Meta:
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی‌ها'
        ordering = ['parent__id', 'position']
    
    def __str__(self):
        return self.title
    
    objects = CategoryManager()

class articles(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش‌نویس'),
        ('p', 'منتشر شده')
    )
    title = models.CharField(max_length=200, verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=100, unique = True, verbose_name="آدرس مقاله")
    description = models.TextField(verbose_name="محتوا")
    category = models.ManyToManyField(Category, verbose_name="دسته‌بندی", related_name="articles")
    thumbnail = models.ImageField(upload_to='Images', verbose_name="تصویر")
    publish = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت")
    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering = ['-publish']
        
    def __str__(self):
        return self.title
    
    def jpublish(self):
        return jalali_converter(self.publish)
    
    jpublish.short_description = 'زمان انتشار'
    
    def category_published(self):
        return self.category.filter(status=True)
    
    def thumbnail_tag(self):
        return format_html("<img width='100' hieght='75' src='{}'>".format(self.thumbnail.url))
    thumbnail_tag.short_description = 'عکس'

    objects = ArticleManager()