# Create Context Menu Data
from quick_docs_drf.settings import DEFAULT
from django.core.exceptions import ImproperlyConfigured
from django.utils.module_loading import import_string


def context_menu():
    """generate context menu data"""

    APP_NAME = set()
    MENU_CONTEXT = []
    base_router = DEFAULT.get("BASE_ROUTER_NAME")
    if base_router is None:
        raise ImproperlyConfigured("BASE_ROUTER_NAME not found in settings.py")
    base_router = import_string(base_router)
    for url in base_router.urls:
        try:
            if url.name not in APP_NAME:
                APP_NAME.add(url.name)
                MENU_CONTEXT.append(
                    {
                        "model": url.callback.cls.queryset.model.__name__,
                        "app_name": url.name,
                        "docs": url.callback.cls.__doc__,
                        "app_actions": [
                            action for action in url.callback.actions.values()
                        ],
                    }
                )
        except AttributeError:
            MENU_CONTEXT.append(
                {
                    "name": url.callback.view_class.__name__,
                    "app_name": url.name,
                    "docs": url.callback.view_class.__doc__,
                }
            )
    return MENU_CONTEXT


def viewset_context():
    """generate viewset context data"""
    VIEWSETS_CONTEXT = []

    viewsets = DEFAULT.get("VIEWSET_LISTS")
    if viewsets is None:
        raise ImproperlyConfigured("VIEWSET_LISTS not found in settings.py")
    for viewset in viewsets:
        viewset = import_string(viewset)
        VIEWSETS_CONTEXT.append(
            {
                "name": viewset.__name__,
                "docs": viewset.__doc__,
                "serializer_class": viewset.serializer_class.__name__,
                "fields": viewset.serializer_class.Meta.fields,
                "permission_classes": [
                    permission.__name__ for permission in viewset.permission_classes
                ],
                "pagination_class": (
                    viewset.pagination_class.__name__
                    if viewset.pagination_class
                    else None
                ),
                "authentication_classes": [
                    authentication.__name__
                    for authentication in viewset.authentication_classes
                ],
                "lookup_field": viewset.lookup_field,
                "throttle_classes": [
                    throttle.__name__ for throttle in viewset.throttle_classes
                ],
                "renderer_classes": [
                    renderer.__name__ for renderer in viewset.renderer_classes
                ],
            }
        )
    return VIEWSETS_CONTEXT


def get_contexts():
    """get menu and viewset"""
    return context_menu(), viewset_context()
