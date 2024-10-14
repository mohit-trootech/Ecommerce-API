from quick_docs_drf.views import documentation_view
from django.urls import path

quick_docs_urls = [
    path("documentation/", documentation_view, name="documentation"),
]
