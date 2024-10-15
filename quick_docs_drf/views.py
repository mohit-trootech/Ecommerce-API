from django.views.generic import TemplateView
from typing import Any
from quick_docs_drf.utils import context as context_utils


class DocumentationView(TemplateView):
    template_name = "quick_docs_drf/documentation.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(
            **kwargs
        ) | context_utils.generate_documentation_page_context_data(self)

        return context


documentation_view = DocumentationView.as_view()
