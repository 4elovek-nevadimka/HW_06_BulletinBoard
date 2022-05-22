from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    content = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return f'/board/articles/{self.id}'

    def __str__(self):
        return self.title


class UserResponse(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=256)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
