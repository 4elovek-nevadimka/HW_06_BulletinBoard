from collections import defaultdict
from datetime import datetime, timedelta

from django.core import mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import UserResponse


def send_email_by_signal(new_response):
    mail_messages = [create_response_mail_message(new_response)]
    send_multiple_emails(mail_messages)


# def send_email_by_scheduler():
#     subscribers_posts = defaultdict(list)
#     today = datetime.now()
#     week_ago = today - timedelta(days=7)
#     for post in Post.objects.filter(creation_date__range=[week_ago, today]):
#         for category in post.categories.all():
#             for subscriber in category.subscribers.all():
#                 subscribers_posts[subscriber].append(post)
#
#     mail_messages = []
#     for subscriber in subscribers_posts.keys():
#         mail_messages.append(create_weekly_mail_message(subscriber, subscribers_posts[subscriber]))
#     send_multiple_emails(mail_messages)


def send_multiple_emails(mail_messages):
    if len(mail_messages) > 0:
        connection = mail.get_connection()
        connection.send_messages(mail_messages)


def create_response_mail_message(new_response):

    html_content = render_to_string(
        'emails/mail_new_response_notification.html',
        {
            'response': new_response,
            'user': new_response.author,
        }
    )
    msg = EmailMultiAlternatives(
        subject=f'Новый отклик по объявлению: {new_response.article__title}',
        body=new_response.text,
        from_email='skillfactorymailserver@yandex.ru',
        to=[new_response.article__author.email],
    )
    msg.attach_alternative(html_content, "text/html")
    return msg


def create_weekly_mail_message(subscriber, weekly_posts):
    html_content = render_to_string(
        'mail_weekly_notification.html',
        {
            'weekly_posts': weekly_posts,
            'user': subscriber,
        }
    )
    msg = EmailMultiAlternatives(
        subject='Your weekly collection of publications',
        body='some text in body',
        from_email='skillfactorymailserver@yandex.ru',
        to=[subscriber.email],
    )
    msg.attach_alternative(html_content, "text/html")
    return msg
