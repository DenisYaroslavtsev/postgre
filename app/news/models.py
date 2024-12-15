from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Category name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    date_posted = models.DateTimeField(auto_now_add=True, verbose_name='Date of publication')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Date of update')
    is_published = models.BooleanField(default=True, verbose_name='Published')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Category', default=1)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'nNews'

