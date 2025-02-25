"""Default Settings for Quick Docs DRF"""

from django.conf import settings


def quick_docs_drf_configuration(key):
    """
    Get Configuration Settings from Project Settings File else None

    :param key: str
    """
    try:
        configuration = settings.QUICK_DOCS_DRF
        return configuration.get(key, None)
    except AttributeError as err:
        raise AttributeError("QUICK_DOCS_DRF not found in settings.py")


DEFAULT = {
    "TITLE": quick_docs_drf_configuration("TITLE") or "Documentation",
    "DESCRIPTION": quick_docs_drf_configuration("DESCRIPTION")
    or "Project Description Not Available",
    "VERSION": quick_docs_drf_configuration("VERSION") or 1.0,
    "AUTHOR": quick_docs_drf_configuration("AUTHOR") or None,
    "AUTHOR_EMAIL": quick_docs_drf_configuration("AUTHOR_EMAIL") or None,
    "LICENSE": quick_docs_drf_configuration("LICENSE") or "MIT",
    "API_URL": quick_docs_drf_configuration("API_URL") or "/api/",
    "BASE_ROUTER_NAME": quick_docs_drf_configuration("BASE_ROUTER_NAME") or None,
    "NESTED_ROUTER_NAME": quick_docs_drf_configuration("NESTED_ROUTER_NAME") or None,
    "VIEWSET_LISTS": quick_docs_drf_configuration("VIEWSET_LISTS") or None,
    "TEMPLATE_STYLE": quick_docs_drf_configuration("TEMPLATE_STYLE") or "bootstrap5",
    "SOCIAL_MEDIA": quick_docs_drf_configuration("SOCIAL_MEDIA") or None,
}
