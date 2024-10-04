from django.contrib import admin
from accounts.models import User
from utils.constants import AdminAction
from django.contrib import messages
from django.utils.translation import ngettext


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "is_active"]
    readonly_fields = [
        "id",
        "date_joined",
        "last_login",
    ]
    fieldsets = [
        (
            "Customer Info",
            {
                "fields": [
                    "id",
                    "first_name",
                    "last_name",
                    "username",
                    "email",
                    "password",
                    "phone",
                    "address",
                    "age",
                    "gender",
                ]
            },
        ),
        (
            "Status Info",
            {
                "classes": ["collapse"],
                "fields": ["is_staff", "is_superuser", "is_active"],
            },
        ),
        (
            "Login Info",
            {"classes": ["collapse"], "fields": ["date_joined", "last_login"]},
        ),
        (
            "Group Info",
            {"classes": ["collapse"], "fields": ["groups", "user_permissions"]},
        ),
    ]
    search_fields = ["username", "first_name", "last_name"]
    list_filter = [
        "is_staff",
        "is_active",
        "is_superuser",
    ]
    ordering = ["id"]
    filter_horizontal = [
        "groups",
        "user_permissions",
    ]
    actions = ["mark_inactive", "mark_active"]

    @admin.action(description=AdminAction.USER_ADMIN_STATUS_UNACTIVE_DESCRIPTION.value)
    def mark_inactive(self, request, queryset):
        updated = queryset.update(is_active=AdminAction.STATUS_INACTIVE.value)
        self.message_user(
            request,
            ngettext(
                AdminAction.USER_INACTIVE_SUCCESS_MESSAGE.value,
                updated,
            )
            % updated,
            messages.SUCCESS,
        )

    @admin.action(description=AdminAction.USER_ADMIN_STATUS_ACTIVE_DESCRIPTION.value)
    def mark_active(self, request, queryset):
        updated = queryset.update(is_active=AdminAction.STATUS_ACTIVE.value)
        self.message_user(
            request,
            ngettext(
                AdminAction.USER_ACTIVE_SUCCESS_MESSAGE.value,
                updated,
            ),
        )
