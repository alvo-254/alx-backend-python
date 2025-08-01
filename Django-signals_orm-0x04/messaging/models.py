from django.db import models
from django.contrib.auth.models import User

class UnreadMessagesManager(models.Manager):
    def for_user(self, user):
        return self.get_queryset().filter(receiver=user, read=False).only('id', 'sender', 'content', 'timestamp')

# ✅ Must come after Message is defined, not inside the manager
# Moved this __str__ method to MessageHistory where it belongs

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)
    read = models.BooleanField(default=False)

    objects = models.Manager()  # default manager
    unread = UnreadMessagesManager()  # ✅ custom manager

    parent_message = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='replies'
    )

    def __str__(self):
        return f"From {self.sender.username} to {self.receiver.username}"


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}"


class MessageHistory(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='history')
    old_content = models.TextField()
    read = models.BooleanField(default=False)  # ✅ New field
    edited_at = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='history_sent')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='history_received')

    def __str__(self):
        return f"Edit history for message ID {self.message.id}"
