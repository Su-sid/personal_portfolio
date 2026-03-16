from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from main_app.models import (
    BlogPost,
    ContactInquiry,
    Project,
    Service,
    Technology,
)


class PortfolioApiTests(APITestCase):
    def setUp(self):
        Service.objects.create(
            title="Web Development",
            summary="High-performance product websites",
            description="Build and optimize websites for conversion.",
            display_order=1,
        )
        Project.objects.create(
            title="Portfolio Platform",
            description="A full-stack portfolio platform",
            category="web",
            is_featured=True,
        )
        BlogPost.objects.create(
            title="How I structure client projects",
            slug="how-i-structure-client-projects",
            excerpt="A practical approach to discovery and delivery.",
            content="Long-form content",
            tags="delivery,process",
            is_published=True,
        )

    def test_health_check(self):
        response = self.client.get(reverse("api-health"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_landing_payload(self):
        response = self.client.get(reverse("api-landing"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["services"]), 1)
        self.assertEqual(len(response.data["featured_projects"]), 1)
        self.assertEqual(len(response.data["latest_posts"]), 1)

    def test_contact_submission(self):
        payload = {
            "full_name": "Test User",
            "email": "test@example.com",
            "message": "Need a website revamp.",
        }
        response = self.client.post(reverse("api-contact"), payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ContactInquiry.objects.count(), 1)


class SeedCommandTests(TestCase):
    def test_seed_projects_is_idempotent(self):
        call_command("seed_projects")
        call_command("seed_projects")

        self.assertEqual(Project.objects.count(), 3)
        self.assertEqual(Project.objects.filter(is_featured=True).count(), 3)
        self.assertGreaterEqual(Technology.objects.count(), 5)
        self.assertTrue(
            all(project.technologies_used.exists() for project in Project.objects.all())
        )

    def test_seed_site_content_is_idempotent(self):
        call_command("seed_site_content")
        call_command("seed_site_content")

        self.assertEqual(Service.objects.count(), 3)
        self.assertEqual(BlogPost.objects.filter(is_published=True).count(), 3)
        self.assertTrue(
            all(
                service.icon.startswith("i-lucide-")
                for service in Service.objects.all()
            )
        )
        self.assertTrue(
            all(
                len(service.description.split()) > 20
                for service in Service.objects.all()
            )
        )
