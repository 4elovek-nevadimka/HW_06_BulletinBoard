import random

import redis

from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import CreateView, FormView

from .forms import BaseRegisterForm, BaseVerificationForm


class BaseRegisterView(FormView):
    form_class = BaseRegisterForm
    success_url = '/sign/sign-up-verify/'

    def form_valid(self, form):
        code = random.randint(0, 999999)
        print(f'code: {code}')

        # sendmail
        red = redis.Redis(host='127.0.0.1', port=6379)
        red.set(code, f"{form.cleaned_data['username']}\t"
                      f"{form.cleaned_data['email']}\t"
                      f"{form.cleaned_data['password1']}", 30)

        return super().form_valid(form)


class BaseVerificationView(CreateView):
    model = User
    form_class = BaseVerificationForm
    success_url = '/sign/sign-in/'

    def form_valid(self, form):
        print(form.cleaned_data['one_time_code'])

        print(form.cleaned_data['username'])
        print(form.cleaned_data['email'])
        print(form.cleaned_data['password1'])

        return super().form_valid(form)


def create_something_view(request):

    return render(request, 'sign/temp.html')
