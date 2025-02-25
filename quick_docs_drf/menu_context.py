from quick_docs_drf.field_types import _field_types
from django.core.exceptions import ImproperlyConfigured
from django.utils.module_loading import import_string
from quick_docs_drf.settings import DEFAULT


# Constant to indicate all fields
ALL = "__all__"


class QuickDocsMenu:
    """
    Generate Quick Docs Menu Context
    """

    def __init__(self) -> None:
        self.context: list = []
        self.app_name: set = set()

    def get_context_menu(self):
        """
        Generate Quick Docs Menu Context
        """
        # Get Base Router from Default Setting
        base_router: str = DEFAULT.get("BASE_ROUTER_NAME")
        if base_router is None:
            # Raise Exception if Not Available
            raise ImproperlyConfigured("BASE_ROUTER_NAME not found in settings.py")
        # Else Import Router
        base_router = import_string(base_router)
        for url in base_router.urls:
            try:
                if url.name not in self.app_name:
                    # Temporary Instance for Multiple Usage
                    viewset = url.callback.cls
                    self.app_name.add(url.name)
                    model = viewset.queryset.model

                    # Generate Context Dict
                    self.context.append(
                        {
                            "model": model.__name__,
                            "app_name": url.name,
                            "docs": viewset.__doc__,
                            "app_actions": [
                                action for action in url.callback.actions.values()
                            ],
                            "lookup_field": viewset.lookup_field,
                            "pagination": (True if viewset.pagination_class else False),
                            "field_types": _field_types.get_field_types(
                                self.get_fields(viewset, model)
                            ),
                            "field_patterns": _field_types.get_field_pattern(
                                self.get_fields(viewset, model)
                            ),
                        }
                    )
            except AttributeError as err:
                # AttibuteError means API Root View
                self.context.append(
                    {
                        "name": url.callback.view_class.__name__,
                        "app_name": url.name,
                        "docs": url.callback.view_class.__doc__,
                    }
                )
        return self.context

    def get_fields(self, viewset, model):
        """
        Get model Fields from Urls
        """
        if viewset.serializer_class.Meta.fields == ALL:
            return model._meta.fields
        return self.filter_serializer_class_fields(viewset.serializer_class, model)

    def filter_serializer_class_fields(self, serializer, model):
        """
        filter serializer class fields into model fields
        """
        fields = [field for field in model._meta.fields]
        for field in fields:
            if field.name not in serializer.Meta.fields:
                fields.remove(field)
        return fields


_quick_docs_menu = QuickDocsMenu()
