import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('moderator', 'Moderator'),
        ('admin', 'Admin'),
    )

    user_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    phone_number = models.CharField(max_length=15, unique=True, default="0000000000")  # ✅ fixed
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    def __str__(self):
        return f"{self.username} ({self.role})"


class Conversation(models.Model):
    conversation_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    participants = models.ManyToManyField("User", related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation {self.conversation_id}"


class Message(models.Model):
    message_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    conversation = models.ForeignKey("Conversation", on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey("User", on_delete=models.CASCADE, related_name='messages')
    message_body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message {self.message_id} from {self.sender.username}"
