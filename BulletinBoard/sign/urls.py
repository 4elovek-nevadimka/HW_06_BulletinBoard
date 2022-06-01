from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from .views import BaseRegisterView, BaseVerificationView, create_something_view

urlpatterns = [
    path('sign-in/',
         LoginView.as_view(template_name='sign/sign-in.html'), name='sign-in'),
    path('sign-out/',
         LogoutView.as_view(template_name='sign/sign-out.html'), name='sign-out'),
    path('sign-up-register/',
         BaseRegisterView.as_view(template_name='sign/sign-up_register.html'), name='register'),
    path('sign-up-verify/', create_something_view, name='verify')
]
