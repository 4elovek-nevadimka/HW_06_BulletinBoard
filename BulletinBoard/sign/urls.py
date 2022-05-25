from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

urlpatterns = [
    path('sign-in/',
         LoginView.as_view(template_name='sign/sign-in.html'), name='sign-in'),
    path('sign-out/',
         LogoutView.as_view(template_name='sign/sign-out.html'), name='sign-out')
]
