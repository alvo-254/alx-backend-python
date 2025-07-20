from rest_framework import viewsets
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer

class ConversationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows conversations to be viewed or edited.
    """
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or created.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
