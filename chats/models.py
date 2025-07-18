from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    """
    Extends Django's built‑in user. Add profile fields as needed.
    """
    display_name = models.CharField(max_length=50, blank=True)
    # avatar = models.ImageField(upload_to='avatars/', blank=True)


class Conversation(models.Model):
    """
    A private or group chat linking two or more users.
    """
    participants = models.ManyToManyField(User, related_name="conversations")
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Chat #{self.pk} ({self.participants.count()} users)"


class Message(models.Model):
    """
    Individual message inside a conversation.
    """
    conversation = models.ForeignKey(
        Conversation, related_name="messages", on_delete=models.CASCADE
    )
    sender = models.ForeignKey(
        User, related_name="sent_messages", on_delete=models.CASCADE
    )
    text = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("sent_at",)

    def __str__(self):
        return f"{self.sender.username}: {self.text[:30]}"
