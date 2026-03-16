from django.urls import path

from apps.accounts.views import UserListView, UserRegistrationView

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="user-register"),
    path("users/", UserListView.as_view(), name="user-list"),
]
