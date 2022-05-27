from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import ArticleForm, UserResponseForm
from .models import Article, UserResponse
from .tasks import response_apply_mail_notification


class ArticleList(ListView):
    model = Article
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'
    ordering = ['-id']
    paginate_by = 5


class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    queryset = Article.objects.all()


# class PostCreateView(PermissionRequiredMixin, CreateView):
class ArticleCreateView(CreateView):
    # permission_required = ('news.add_post',)
    form_class = ArticleForm
    template_name = 'articles/article_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


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
    form_class = UserResponseForm
    template_name = 'user_responses/response_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.article = Article.objects.get(pk=self.kwargs['a_id'])
        return super().form_valid(form)


class UserResponseDetailView(DetailView):
    template_name = 'user_responses/response_detail.html'
    queryset = UserResponse.objects.all()


class UserResponseDeleteView(DeleteView):
    template_name = 'user_responses/response_delete.html'
    queryset = UserResponse.objects.all()
    success_url = '/account/outbox/'


class AccountMyArticlesView(LoginRequiredMixin, ListView):
    template_name = 'account/account_my_articles.html'
    model = Article
    context_object_name = 'items_list'
    ordering = ['-id']
    paginate_by = 5

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)


class AccountInboxView(LoginRequiredMixin, ListView):
    template_name = 'account/account_inbox.html'
    model = UserResponse
    context_object_name = 'items_list'
    ordering = ['-id']
    paginate_by = 5

    def get_queryset(self):
        return super().get_queryset().filter(article__author=self.request.user)


class AccountOutboxView(LoginRequiredMixin, ListView):
    template_name = 'account/account_outbox.html'
    model = UserResponse
    context_object_name = 'items_list'
    ordering = ['-id']
    paginate_by = 5

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)


@login_required
def response_apply(request, r_id):
    response = UserResponse.objects.get(pk=r_id)
    response.status = True
    response.save()
    response_apply_mail_notification.delay(r_id)
    return redirect('/board/account/inbox/')
