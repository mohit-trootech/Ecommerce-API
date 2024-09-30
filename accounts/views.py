from django.views.generic import View, UpdateView, FormView
from utils.constants import Templates, Urls, Success, Errors
from accounts.forms import UserLoginForm, UserCreationForm, UserUpdateForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.messages import info
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from accounts.models import User
from utils.utils import force_logout
from typing import Any
from django.shortcuts import redirect


class LogoutView(View):

    def get(self, request):
        """
        logout user from request
        """
        logout(request)
        info(request, Success.LOGGED_OUT.value)
        return redirect(Urls.LOGIN.value)


logout_view = LogoutView.as_view()


class ForceLogoutView(View):

    def get(self, request):
        """
        logout user from request
        """
        force_logout(request)
        info(request, Success.FORCE_LOGGED_OUT.value)
        return redirect(Urls.LOGIN.value)


force_logout_view = ForceLogoutView.as_view()


class ProfileView(UpdateView):
    form_class = UserUpdateForm
    model = User
    template_name = Templates.PROFILE.value
    success_url = Urls.PROFILE_SUCCESS_URL.value

    def get_success_url(self) -> str:
        """
        get success url based on login user details
        """
        info(self.request, Success.PROFILE_UPDATED.value)
        return self.success_url.format(pk=self.request.user.pk)


profile_view = ProfileView.as_view()


class LoginView(FormView):
    template_name = Templates.LOGIN.value
    form_class = UserLoginForm
    success_url = reverse_lazy(Urls.TODOS_HOME.value)

    def form_valid(self, form):
        """
        login form handle, user will log in if details form is valid else if user not exist return form_invalid

        :param form: _description_
        :return: _description_
        """
        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"],
        )
        if not user:
            form.add_error(None, Errors.LOGIN_ERROR.value)
            return super().form_invalid(form)
        login(self.request, user)
        info(self.request, Success.LOGGED_IN.value)
        return super().form_valid(form)


login_view = LoginView.as_view()


class RegistrationView(FormView):
    template_name = Templates.SIGNUP.value
    form_class = UserCreationForm
    success_url = reverse_lazy(Urls.LOGIN_REVERSE.value)

    def form_valid(self, form):
        """
        registration form handle, user signed up if form_valid else if password not match user already exist or password valiadtion return form_invalid
        """
        try:
            if self.request.POST.get("terms") is None:
                form.add_error(None, Errors.TERMS_NOT_ACCEPTED.value)
                return super().form_invalid(form)
            password1 = self.request.POST.get("password1")
            password2 = self.request.POST.get("password2")
            validate_password(password1)
            if not password1 == password2:
                form.add_error(None, Errors.PASSWORD_NOT_MATCH.value)
                return super().form_invalid(form)
            user = form.save(commit=False)
            user.set_password(password1)
            user.save()
            info(self.request, Success.SIGNED_UP.value)
            return super().form_valid(form)
        except ValidationError as ve:
            form.add_error(None, ve)
            return super().form_invalid(form)


registration_view = RegistrationView.as_view()


class UpdateApiKeyView(View):

    def get(self, request, *args: Any, **kwargs: Any) -> Any:
        from uuid import uuid4

        request.user.api_key = uuid4()
        request.user.save()
        info(request, Success.API_KEY_UPDATED.value)
        return redirect(Urls.PROFILE_SUCCESS_URL.value.format(pk=request.user.pk))


update_api_view = UpdateApiKeyView.as_view()
