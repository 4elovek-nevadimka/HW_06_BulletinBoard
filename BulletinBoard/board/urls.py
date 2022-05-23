from django.urls import path

from .views import ArticleList, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView, \
    UserResponseCreateView

urlpatterns = [
    # Список всех объявлений
    path('articles/', ArticleList.as_view(), name='article_list'),
    # Конкретное объявление
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    # Добавление объявления
    path('articles/add/', ArticleCreateView.as_view(), name='article_add'),
    # Редактирование объявления
    path('articles/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_update'),
    # Удаление объявления
    path('articles/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),

    # Добавление отклика
    path('responses/add/', UserResponseCreateView.as_view(), name='user_response_add'),

    # path('account/', AccountView.as_view(), name='account'),

    # path('subscribe/<int:cat_id>', subscribe_me, name='subscribe'),
    # path('unsubscribe/<int:cat_id>', unsubscribe_me, name='unsubscribe'),
]
