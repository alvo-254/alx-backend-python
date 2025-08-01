from django.urls import path
from .views import delete_user
from .views import conversation_view
from .views import unread_messages_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('delete-user/<int:user_id>/', delete_user, name='delete_user'),
]

urlpatterns = [
    path('conversation/', conversation_view, name='conversation'),
    path('delete-user/<int:user_id>/', delete_user, name='delete_user'),
    path('delete-user/<int:user_id>/', delete_user, name='delete_user'),
    path('unread/', unread_messages_view, name='unread_messages'),

    # ✅ Add this:
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

]
