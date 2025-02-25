"""Generate Documentation Page Context Data"""

from quick_docs_drf.utils import utils
from quick_docs_drf.utils.context_menu import get_contexts
from quick_docs_drf.menu_context import _quick_docs_menu


def generate_documentation_page_context_data(self):
    """Generate Documentation Page Context Data"""
    menu_context, viewset_context = get_contexts()
    return {
        "template_style": utils.get_template_styling(),
        "project_name": utils.get_project_name(),
        "project_description": utils.get_project_description(),
        "project_version": utils.get_project_version(),
        "project_author": utils.get_project_author(),
        "project_author_email": utils.get_project_author_email(),
        "project_license": utils.get_project_license(),
        "api_url": utils.get_api_url(),
        "social_media": utils.get_social_media(),
        "menu_context": _quick_docs_menu.get_context_menu(),
        "viewset_context": viewset_context,
    }
