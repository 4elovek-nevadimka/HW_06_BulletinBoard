from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import UserResponse
from .tasks import new_response_mail_notification


@receiver(post_save, sender=UserResponse)
def notify_post_created(sender, instance, created, **kwargs):
    if created:
        new_response_mail_notification.delay(instance.id)
