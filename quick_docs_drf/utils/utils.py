"""Utility Function for Quick Docs DRF"""

from quick_docs_drf.settings import DEFAULT


def get_template_styling():
    """Base Documentation Template Styling"""
    return DEFAULT.get("TEMPLATE_STYLE")


def get_project_name():
    """Documentation Project Name"""
    return DEFAULT.get("TITLE")


def get_project_description():
    """Documentation Project Description"""
    return DEFAULT.get("DESCRIPTION")


def get_project_version():
    """Documentation Project Version"""
    return DEFAULT.get("VERSION")


def get_project_author():
    """Documentation Project Author"""
    return DEFAULT.get("AUTHOR")


def get_project_author_email():
    """Documentation Project Author Email"""
    return DEFAULT.get("AUTHOR_EMAIL")


def get_project_license():
    """Documentation Project License"""
    return DEFAULT.get("LICENSE")


def get_api_url():
    """Documentation API URL"""
    return DEFAULT.get("API_URL")


def get_social_media():
    """Documentation Social Details"""
    return DEFAULT.get("SOCIAL_MEDIA")
