from django.urls import path

from .views import ArticleList, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView, \
    model_form_view

urlpatterns = [
    # Список всех объявлений
    path('', ArticleList.as_view(), name='article_list'),
    # Конкретное объявление
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    # Добавление объявления
    path('add/', ArticleCreateView.as_view(), name='article_add'),
    # Редактирование объявления
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_update'),
    # Удаление объявления
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),

    path('test_form/', model_form_view),

    # path('account/', AccountView.as_view(), name='account'),

    # path('subscribe/<int:cat_id>', subscribe_me, name='subscribe'),
    # path('unsubscribe/<int:cat_id>', unsubscribe_me, name='unsubscribe'),
]
