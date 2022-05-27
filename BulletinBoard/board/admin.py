from django.contrib import admin

from .models import Article, Category, UserResponse


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(UserResponse)
class UserResponseAdmin(admin.ModelAdmin):
    pass
