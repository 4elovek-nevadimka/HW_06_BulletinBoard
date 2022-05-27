from django.urls import path

from .views import ArticleList, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView, \
    UserResponseCreateView, AccountMyArticlesView, AccountInboxView, AccountOutboxView, UserResponseDetailView, \
    UserResponseDeleteView, response_apply

urlpatterns = [
    # Список всех объявлений
    path('articles/', ArticleList.as_view(), name='article_list'),
    # Страница объявления
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    # Добавление объявления
    path('articles/add/', ArticleCreateView.as_view(), name='article_add'),
    # Редактирование объявления
    path('articles/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_update'),
    # Удаление объявления
    path('articles/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),

    # Добавление отклика
    path('responses/add/<int:a_id>/', UserResponseCreateView.as_view(), name='user_response_add'),
    # Страница с откликом
    path('responses/<int:pk>/', UserResponseDetailView.as_view(), name='user_response_detail'),
    # Удаление отклика
    path('responses/<int:pk>/delete/', UserResponseDeleteView.as_view(), name='user_response_delete'),

    path('account/my_articles/', AccountMyArticlesView.as_view(), name='account_my_articles'),
    path('account/inbox/', AccountInboxView.as_view(), name='account_inbox'),
    path('account/outbox/', AccountOutboxView.as_view(), name='account_outbox'),

    path('response_apply/<int:r_id>/', response_apply, name='response_apply'),
    # path('unsubscribe/<int:cat_id>', unsubscribe_me, name='unsubscribe'),
]
