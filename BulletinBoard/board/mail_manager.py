from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.core import mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import Article


def send_email_by_signal(response, apply):
    if apply:
        mail_messages = [response_apply_mail_message(response)]
    else:
        mail_messages = [response_create_mail_message(response)]
    send_multiple_emails(mail_messages)


def send_email_by_scheduler():
    new_articles = list()
    today = datetime.now()
    week_ago = today - timedelta(days=7)
    for article in Article.objects.filter(creation_date__range=[week_ago, today]):
        new_articles.append(article)

    mail_messages = []
    for author in User.objects.exclude(email__isnull=True):
        mail_messages.append(create_weekly_mail_message(author, new_articles))
    send_multiple_emails(mail_messages)


def response_create_mail_message(response):

    return create_mail_message(
        response,
        'emails/mail_new_response_notification.html',
        f'Новый отклик по объявлению: {response.article.title}',
        [response.article.author.email]
    )


def response_apply_mail_message(response):

    return create_mail_message(
        response,
        'emails/mail_apply_response_notification.html',
        f'Принят отклик по объявлению: {response.article.title}',
        [response.author.email]
    )


def create_mail_message(response, template, subject, to):

    html_content = render_to_string(
        template,
        {
            'response': response,
        }
    )
    msg = EmailMultiAlternatives(
        subject=subject,
        body=response.text,
        from_email='skillfactorymailserver@yandex.ru',
        to=to,
    )
    msg.attach_alternative(html_content, "text/html")
    return msg


def create_weekly_mail_message(author, new_articles):
    html_content = render_to_string(
        'mail_weekly_notification.html',
        {
            'weekly_posts': new_articles,
            'user': author,
        }
    )
    msg = EmailMultiAlternatives(
        subject='Your weekly collection of publications',
        body='some text in body',
        from_email='skillfactorymailserver@yandex.ru',
        to=[author.email],
    )
    msg.attach_alternative(html_content, "text/html")
    return msg


def send_multiple_emails(mail_messages):
    if len(mail_messages) > 0:
        connection = mail.get_connection()
        connection.send_messages(mail_messages)
