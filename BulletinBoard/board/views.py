from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import ArticleForm
from .models import Article


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
