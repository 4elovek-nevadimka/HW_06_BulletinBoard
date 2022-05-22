from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import ArticleForm
from .models import Article


class ArticleList(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'
    # ordering = ['-id']
    # paginate_by = 10


class ArticleDetailView(DetailView):
    template_name = 'article_detail.html'
    # queryset = Post.objects.all()


# class PostCreateView(PermissionRequiredMixin, CreateView):
class ArticleCreateView(CreateView):
    # permission_required = ('news.add_post',)
    template_name = 'article_create.html'
    form_class = ArticleForm


# class ArticleUpdateView(PermissionRequiredMixin, UpdateView):
class ArticleUpdateView(UpdateView):
    # permission_required = ('news.change_post',)
    template_name = 'article_update.html'
    # form_class = PostForm

    # def get_object(self, **kwargs):
    #     return Post.objects.get(pk=self.kwargs.get('pk'))


class ArticleDeleteView(DeleteView):
    template_name = 'article_delete.html'
    # queryset = Post.objects.all()
    # success_url = '/news/'
