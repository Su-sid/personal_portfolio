from django.urls import path

from .api_views import (
    BlogPostDetailView,
    BlogPostListView,
    ContactInquiryCreateView,
    HealthCheckView,
    PortfolioLandingView,
    ProjectListView,
    ResumeView,
    ServiceListView,
    SiteConfigView,
)

urlpatterns = [
    path("health/", HealthCheckView.as_view(), name="api-health"),
    path("config/", SiteConfigView.as_view(), name="api-config"),
    path("landing/", PortfolioLandingView.as_view(), name="api-landing"),
    path("services/", ServiceListView.as_view(), name="api-services"),
    path("projects/", ProjectListView.as_view(), name="api-projects"),
    path("resume/", ResumeView.as_view(), name="api-resume"),
    path("blog/", BlogPostListView.as_view(), name="api-blog-list"),
    path("blog/<slug:slug>/", BlogPostDetailView.as_view(), name="api-blog-detail"),
    path("contact/", ContactInquiryCreateView.as_view(), name="api-contact"),
]
