from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from .models import Message
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from django.views.decorators.cache import cache_page
from django.contrib.auth import views as auth_views


@cache_page(60)  # Cache the view for 60 seconds
@login_required
def conversation_view(request):
    top_level = Message.objects.filter(parent_message__isnull=True).select_related('sender', 'receiver').prefetch_related(
        Prefetch('replies', queryset=Message.objects.select_related('sender', 'receiver'))
    )
    return render(request, 'conversation.html', {'messages': top_level})


def delete_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        return HttpResponse(f"User {user.username} and related data deleted.")
    except User.DoesNotExist:
        return HttpResponse("User not found.", status=404)

@login_required
def conversation_view(request):
    # Only fetch top-level messages and their replies
    top_level = Message.objects.filter(parent_message__isnull=True).select_related('sender', 'receiver').prefetch_related(
        Prefetch('replies', queryset=Message.objects.select_related('sender', 'receiver'))
    )
    return render(request, 'conversation.html', {'messages': top_level})

@login_required
def unread_messages_view(request):
    unread = Message.unread.for_user(request.user)
    return render(request, 'unread_messages.html', {'messages': unread})