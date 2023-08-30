from django.urls import path
from .views import CustomUserListCreateAPIView, CustomUserDetailAPIView

urlpatterns = [
    path('all-users', CustomUserListCreateAPIView.as_view(), name="all-users"),
    path('user/<int:pk>', CustomUserDetailAPIView.as_view(), name="user")
]