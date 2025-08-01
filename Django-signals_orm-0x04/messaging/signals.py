from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Message, Notification, MessageHistory


@receiver(post_delete, sender=User)
def delete_user_related_data(sender, instance, **kwargs):
    # Delete related messages
    Message.objects.filter(sender=instance).delete()
    Message.objects.filter(receiver=instance).delete()

    # Delete notifications
    Notification.objects.filter(user=instance).delete()


@receiver(post_save, sender=Message)
def notify_receiver(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.receiver,
            message=instance,
            content=f"New message from {instance.sender.username}"
        )


@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    if instance.pk:  # Only if the message already exists
        try:
            old_instance = Message.objects.get(pk=instance.pk)
            if old_instance.content != instance.content:
                MessageHistory.objects.create(
                    message=old_instance,
                    old_content=old_instance.content
                )
                instance.edited = True
        except Message.DoesNotExist:
            pass
