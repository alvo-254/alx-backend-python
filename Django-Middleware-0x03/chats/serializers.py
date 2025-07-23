from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Conversation, Message

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(read_only=True)
    phone_number = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['user_id', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def validate_phone_number(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Phone number must contain only digits.")
        return value


class MessageSerializer(serializers.ModelSerializer):
    message_id = serializers.CharField(read_only=True)
    sender = UserSerializer(read_only=True)
    message_body = serializers.CharField()
    sent_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Message
        fields = ['message_id', 'conversation', 'sender', 'message_body', 'sent_at']


class ConversationSerializer(serializers.ModelSerializer):
    conversation_id = serializers.CharField(read_only=True)
    participants = UserSerializer(many=True, read_only=True)
    messages = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'created_at', 'messages']

    def get_messages(self, obj):
        messages = obj.messages.all()
        return MessageSerializer(messages, many=True).data
