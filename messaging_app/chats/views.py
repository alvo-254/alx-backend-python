from django_filters.rest_framework import DjangoFilterBackend
from .filters import MessageFilter
from .pagination import CustomPagination
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .models import Message, Conversation
from .serializers import MessageSerializer, ConversationSerializer
from .permissions import IsParticipantOfConversation
from .filters import MessageFilter
from .pagination import CustomPagination


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]
    filter_backends = [DjangoFilterBackend]
    filterset_class = MessageFilter
    pagination_class = CustomPagination

    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(conversation__participants=user)
