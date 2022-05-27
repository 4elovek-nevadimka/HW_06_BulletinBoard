from django.forms import ModelForm

from .models import Article, UserResponse


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category']


class UserResponseForm(ModelForm):
    class Meta:
        model = UserResponse
        fields = ['text']
