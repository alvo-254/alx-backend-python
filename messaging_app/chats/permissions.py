# chats/permissions.py

from rest_framework.permissions import BasePermission, SAFE_METHODS

# chats/permissions.py
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsParticipantOfConversation(BasePermission):
    """
    Allow only participants of a conversation to access or modify messages.
    """

    def has_object_permission(self, request, view, obj):
        user = request.user

        # ✅ Check if user is authenticated
        if not user or not user.is_authenticated:
            return False

        # ✅ Check if user is a participant
        return user in obj.conversation.participants.all()


class IsParticipantOfConversation(BasePermission):
    """
    Custom permission: only allow participants of a conversation to interact.
    """

    def has_object_permission(self, request, view, obj):
        user = request.user

        # Allow viewing if user is in the conversation
        if request.method in SAFE_METHODS:
            return user in obj.conversation.participants.all()

        # Allow update/delete only if user is in the conversation
        if request.method in ["PUT", "PATCH", "DELETE"]:
            return user in obj.conversation.participants.all()

        # For POST (send message), also check participation
        if request.method == "POST":
            return user in obj.conversation.participants.all()

        return False
