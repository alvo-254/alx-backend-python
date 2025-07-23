# chats/permissions.py

from rest_framework import permissions
from .models import Conversation

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Allows access only to participants of the conversation.
    """

    def has_permission(self, request, view):
        # Check if user is authenticated
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
        Check if the user is a participant of the conversation for object-level operations.
        Assumes the object is a Message or Conversation instance.
        """
        # If it's a Message instance
        if hasattr(obj, "conversation"):
            return request.user in obj.conversation.participants.all()

        # If it's a Conversation instance
        if isinstance(obj, Conversation):
            return request.user in obj.participants.all()

        return False
