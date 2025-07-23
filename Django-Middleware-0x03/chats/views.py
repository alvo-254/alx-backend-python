# chats/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Message, Conversation
from .serializers import MessageSerializer
from .permissions import IsParticipantOfConversation
from .filters import MessageFilter
from .pagination import CustomPagination
from django.shortcuts import get_object_or_404

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]
    filterset_class = MessageFilter
    pagination_class = CustomPagination

    def get_queryset(self):
        return Message.objects.filter(conversation__participants=self.request.user)

    def perform_create(self, serializer):
        conversation_id = self.request.data.get("conversation")
        conversation = get_object_or_404(Conversation, id=conversation_id)

        if not self.request.user.is_authenticated:
            return Response(
                {"detail": "Authentication required."},
                status=status.HTTP_403_FORBIDDEN
            )

        if self.request.user not in conversation.participants.all():
            return Response(
                {"detail": "Forbidden: You are not a participant of this conversation."},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer.save(sender=self.request.user, conversation=conversation)
