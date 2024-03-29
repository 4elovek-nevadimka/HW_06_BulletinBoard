from celery import shared_task

from .mail_manager import send_email_by_signal, send_email_by_scheduler
from .models import UserResponse


@shared_task
def new_response_mail_notification(new_response_id):
    send_email_by_signal(UserResponse.objects.get(pk=new_response_id), False)
    print("new response notification have been sent...")


@shared_task
def response_apply_mail_notification(response_id):
    send_email_by_signal(UserResponse.objects.get(pk=response_id), True)
    print("response apply notification have been sent...")


@shared_task()
def weekly_mail_notification():
    send_email_by_scheduler()
    print("weekly notification have been sent from celery...")
