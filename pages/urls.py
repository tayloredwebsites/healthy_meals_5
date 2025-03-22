from django.urls import path

from .views import HomePageView, AboutPageView, DocsPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("docs/", DocsPageView.as_view(), name="docs"),
]
