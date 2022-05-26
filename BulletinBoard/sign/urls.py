from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from .views import BaseRegisterView

urlpatterns = [
    path('sign-in/',
         LoginView.as_view(template_name='sign/sign-in.html'), name='sign-in'),
    path('sign-out/',
         LogoutView.as_view(template_name='sign/sign-out.html'), name='sign-out'),
    path('sign-up/',
         BaseRegisterView.as_view(template_name='sign/sign-up.html'), name='sign-up')
]
