from django.urls import path
from accounts.views import (
    login_view,
    logout_view,
    registration_view,
    profile_view,
    force_logout_view,
)
from utils.constants import Urls

urlpatterns = [
    path("login/", login_view, name=Urls.LOGIN_REVERSE.value),
    path("logout/", logout_view, name=Urls.LOGOUT_REVERSE.value),
    path("force_logout/", force_logout_view, name=Urls.FORCE_LOGOUT_REVERSE.value),
    path("signup/", registration_view, name=Urls.REGISTER_REVERSE.value),
    path("profile/<int:pk>/", profile_view, name=Urls.PROFILE_REVERSE.value),
]
