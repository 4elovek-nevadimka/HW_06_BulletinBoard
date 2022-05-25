from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import ArticleForm, UserResponseForm
from .models import Article, UserResponse


class ArticleList(ListView):
    model = Article
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'
    ordering = ['-id']
    paginate_by = 3


class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    queryset = Article.objects.all()


# class PostCreateView(PermissionRequiredMixin, CreateView):
class ArticleCreateView(CreateView):
    # permission_required = ('news.add_post',)
    template_name = 'articles/article_create.html'
    form_class = ArticleForm


# class ArticleUpdateView(PermissionRequiredMixin, UpdateView):
class ArticleUpdateView(UpdateView):
    # permission_required = ('news.change_post',)
    template_name = 'articles/article_update.html'
    form_class = ArticleForm

    def get_object(self, **kwargs):
        return Article.objects.get(pk=self.kwargs.get('pk'))


class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'
    queryset = Article.objects.all()
    success_url = '/board/articles/'


class UserResponseCreateView(CreateView):
    # permission_required = ('news.add_post',)
    template_name = 'user_responses/response_create.html'
    form_class = UserResponseForm


class AccountMyArticlesView(LoginRequiredMixin, ListView):
    template_name = 'account/account_my_articles.html'
    model = Article
    context_object_name = 'items_list'
    ordering = ['-id']

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)


class AccountInboxView(LoginRequiredMixin, ListView):
    template_name = 'account/account_inbox.html'
    model = UserResponse
    context_object_name = 'items_list'
    ordering = ['-id']

    def get_queryset(self):
        return super().get_queryset().filter(article__author=self.request.user)


class AccountOutboxView(LoginRequiredMixin, ListView):
    template_name = 'account/account_outbox.html'
    model = UserResponse
    context_object_name = 'items_list'
    ordering = ['-id']

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)
