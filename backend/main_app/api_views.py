from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Q
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import BlogPost, Education, Experience, ProgrammingLanguage, Project, Service, Skill
from .serializers import (
    BlogPostDetailSerializer,
    BlogPostListSerializer,
    ContactInquirySerializer,
    EducationSerializer,
    ExperienceSerializer,
    ProgrammingLanguageSerializer,
    ProjectSerializer,
    ServiceSerializer,
    SkillSerializer,
)


class HealthCheckView(APIView):
    def get(self, request):
        return Response({"status": "ok"}, status=status.HTTP_200_OK)


class SiteConfigView(APIView):
    def get(self, request):
        return Response(
            {
                "profile": {
                    "name": settings.SITE_OWNER_NAME,
                    "title": settings.SITE_OWNER_TITLE,
                    "tagline": settings.SITE_TAGLINE,
                    "about": settings.SITE_ABOUT,
                },
                "cta": {
                    "calendly_url": settings.CALENDLY_URL,
                    "whatsapp_number": settings.WHATSAPP_NUMBER,
                    "whatsapp_text": settings.WHATSAPP_DEFAULT_TEXT,
                    "contact_email": settings.CONTACT_EMAIL,
                },
                "social": {
                    "linkedin_url": settings.SOCIAL_LINKEDIN_URL,
                    "github_url": settings.SOCIAL_GITHUB_URL,
                    "x_url": settings.SOCIAL_X_URL,
                },
            },
            status=status.HTTP_200_OK,
        )


class ServiceListView(generics.ListAPIView):
    serializer_class = ServiceSerializer

    def get_queryset(self):
        return Service.objects.filter(is_featured=True)


class ProjectListView(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        queryset = Project.objects.prefetch_related("technologies_used")
        featured = self.request.query_params.get("featured")
        if featured in {"1", "true", "True"}:
            queryset = queryset.filter(is_featured=True)
        category = self.request.query_params.get("category")
        if category:
            queryset = queryset.filter(category=category)
        return queryset


class ResumeView(APIView):
    def get(self, request):
        experiences = Experience.objects.all()
        long_experiences = [exp for exp in experiences if not exp.is_short]
        short_experiences = [exp for exp in experiences if exp.is_short]

        return Response(
            {
                "long_experiences": ExperienceSerializer(long_experiences, many=True).data,
                "short_experiences": ExperienceSerializer(short_experiences, many=True).data,
                "education_entries": EducationSerializer(Education.objects.all(), many=True).data,
                "professional_skills": SkillSerializer(
                    Skill.objects.filter(category="PROFESSIONAL"), many=True
                ).data,
                "programming_languages": ProgrammingLanguageSerializer(
                    ProgrammingLanguage.objects.all(), many=True
                ).data,
            },
            status=status.HTTP_200_OK,
        )


class BlogPostListView(generics.ListAPIView):
    serializer_class = BlogPostListSerializer

    def get_queryset(self):
        queryset = BlogPost.objects.filter(is_published=True)
        query = self.request.query_params.get("q")
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query)
                | Q(excerpt__icontains=query)
                | Q(content__icontains=query)
                | Q(tags__icontains=query)
            )
        return queryset


class BlogPostDetailView(generics.RetrieveAPIView):
    serializer_class = BlogPostDetailSerializer
    lookup_field = "slug"

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)


class PortfolioLandingView(APIView):
    def get(self, request):
        latest_posts = BlogPost.objects.filter(is_published=True)[:3]
        featured_projects = Project.objects.filter(is_featured=True).prefetch_related("technologies_used")[:6]
        services = Service.objects.filter(is_featured=True)[:6]

        return Response(
            {
                "services": ServiceSerializer(services, many=True).data,
                "featured_projects": ProjectSerializer(
                    featured_projects, many=True, context={"request": request}
                ).data,
                "latest_posts": BlogPostListSerializer(
                    latest_posts, many=True, context={"request": request}
                ).data,
            },
            status=status.HTTP_200_OK,
        )


class ContactInquiryCreateView(generics.CreateAPIView):
    serializer_class = ContactInquirySerializer

    def perform_create(self, serializer):
        inquiry = serializer.save()
        if settings.EMAIL_HOST and settings.CONTACT_EMAIL:
            send_mail(
                subject=f"Portfolio inquiry from {inquiry.full_name}",
                message=f"From: {inquiry.full_name} <{inquiry.email}>\n\n{inquiry.message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=True,
            )
