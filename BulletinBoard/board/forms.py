from django.forms import ModelForm

from .models import Article


class ArticleForm(ModelForm):

    class Meta:
        model = Article
        fields = ['author', 'title', 'content', 'category']


class QuillPostForm(ModelForm):
    class Meta:
        model = Article
        fields = (
            'content',
        )
