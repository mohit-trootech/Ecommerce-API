# -*- coding: utf-8 -*-
from django.forms import (
    Form,
    ModelForm,
    TextInput,
    CharField,
    PasswordInput,
    NumberInput,
    EmailInput,
    ClearableFileInput,
)
from accounts.models import User
from utils.constants import (
    FORM_LABELS,
    FORM_CLASS,
    FORM_CLASS_FILE,
)


class UserCreationForm(ModelForm):
    class Meta:
        model = User
        fields = ["username"]
        widgets = {
            "username": TextInput(
                attrs={"class": FORM_CLASS, "placeholder": "Enter Username"}
            )
        }
        labels = {
            "username": FORM_LABELS.get("username"),
        }


class UserLoginForm(Form):
    username = CharField(
        required=True,
        max_length=30,
        widget=TextInput(
            attrs={
                "class": FORM_CLASS,
                "placeholder": "Enter Login Username",
                "required": True,
            }
        ),
        label=FORM_LABELS.get("username"),
    )
    password = CharField(
        required=True,
        widget=PasswordInput(
            attrs={
                "class": FORM_CLASS,
                "placeholder": "Enter Login Password",
                "required": True,
            }
        ),
        label=FORM_LABELS.get("password"),
    )


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
        ]
        widgets = {}
        labels = {}
        input_option = TextInput

        for field in fields:
            if field == "email":
                input_option = EmailInput
            widgets[field] = input_option(attrs={"class": FORM_CLASS})
            labels[field] = FORM_LABELS.get(field)
