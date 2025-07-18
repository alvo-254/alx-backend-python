from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer


class ConversationViewSet(viewsets.ModelViewSet):
    """
    list   /conversations/          ↩️ all user’s chats
    create /conversations/          ➕ new chat (with participant ids)
    """
    serializer_class = ConversationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.conversations.all()

    def perform_create(self, serializer):
        convo = serializer.save()
        # Include creator plus supplied participants
        convo.participants.add(self.request.user, *self.request.data.get("participants", []))


class MessageViewSet(viewsets.ModelViewSet):
    """
    list   /messages/?conversation=<id>
    create /messages/               ➕ send message
    """
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        convo_id = self.request.query_params.get("conversation")
        convo = get_object_or_404(Conversation, pk=convo_id, participants=self.request.user)
        return convo.messages.all()

    def perform_create(self, serializer):
        convo_id = self.request.data.get("conversation")
        convo = get_object_or_404(Conversation, pk=convo_id, participants=self.request.user)
        serializer.save(sender=self.request.user, conversation=convo)
