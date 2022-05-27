from collections import defaultdict
from datetime import datetime, timedelta

from django.core import mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import UserResponse


def send_email_by_signal(response, apply):
    if apply:
        mail_messages = [response_apply_mail_message(response)]
    else:
        mail_messages = [response_create_mail_message(response)]
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


def response_create_mail_message(response):

    return create_mail_message(
        response,
        'emails/mail_new_response_notification.html',
        f'Новый отклик по объявлению: {response.article.title}',
        [response.article.author.email]
    )

    # html_content = render_to_string(
    #     'emails/mail_new_response_notification.html',
    #     {
    #         'response': response,
    #     }
    # )
    # msg = EmailMultiAlternatives(
    #     subject=f'Новый отклик по объявлению: {response.article.title}',
    #     body=response.text,
    #     from_email='skillfactorymailserver@yandex.ru',
    #     to=[response.article.author.email],
    # )
    # msg.attach_alternative(html_content, "text/html")
    # return msg


def response_apply_mail_message(response):

    return create_mail_message(
        response,
        'emails/mail_apply_response_notification.html',
        f'Принят отклик по объявлению: {response.article.title}',
        [response.author.email]
    )

    # html_content = render_to_string(
    #     'emails/mail_apply_response_notification.html',
    #     {
    #         'response': response,
    #     }
    # )
    # msg = EmailMultiAlternatives(
    #     subject=f'Принят отклик по объявлению: {response.article.title}',
    #     body=response.text,
    #     from_email='skillfactorymailserver@yandex.ru',
    #     to=[response.author.email],
    # )
    # msg.attach_alternative(html_content, "text/html")
    # return msg


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


# def create_weekly_mail_message(subscriber, weekly_posts):
#     html_content = render_to_string(
#         'mail_weekly_notification.html',
#         {
#             'weekly_posts': weekly_posts,
#             'user': subscriber,
#         }
#     )
#     msg = EmailMultiAlternatives(
#         subject='Your weekly collection of publications',
#         body='some text in body',
#         from_email='skillfactorymailserver@yandex.ru',
#         to=[subscriber.email],
#     )
#     msg.attach_alternative(html_content, "text/html")
#     return msg

def send_multiple_emails(mail_messages):
    if len(mail_messages) > 0:
        connection = mail.get_connection()
        connection.send_messages(mail_messages)
