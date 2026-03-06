from django.core.management.base import BaseCommand
from django.utils.text import slugify

from main_app.models import BlogPost, Service


class Command(BaseCommand):
    help = "Seed services and blog content for the portfolio frontend"

    def handle(self, *args, **kwargs):
        services = [
            {
                "title": "Website Design & Development",
                "summary": "Conversion-focused websites for modern brands.",
                "description": "From discovery and wireframing to final deployment, I build fast and reliable web experiences.",
                "icon": "bi-window-stack",
                "display_order": 1,
            },
            {
                "title": "AI & Automation Solutions",
                "summary": "Custom assistants and automations for business operations.",
                "description": "I integrate AI workflows that reduce repetitive work and unlock better decision-making.",
                "icon": "bi-cpu",
                "display_order": 2,
            },
            {
                "title": "Technical Consulting",
                "summary": "Architecture and delivery support for product teams.",
                "description": "I help teams define scope, choose practical stacks, and ship maintainable systems.",
                "icon": "bi-diagram-3",
                "display_order": 3,
            },
        ]

        for payload in services:
            Service.objects.update_or_create(
                title=payload["title"],
                defaults=payload,
            )

        posts = [
            {
                "title": "How to scope a client website project",
                "excerpt": "A practical checklist to move from vague idea to clear execution plan.",
                "content": "A successful project starts with discovery. Define goals, audience, content needs, and measurable outcomes before development begins.",
                "tags": "web,consulting,delivery",
            },
            {
                "title": "Adding AI features without overengineering",
                "excerpt": "Focus on reliable workflows before complex model orchestration.",
                "content": "AI features should solve one real user pain at a time. Start with constrained use cases and iterate with telemetry.",
                "tags": "ai,product,engineering",
            },
            {
                "title": "Why performance is a business feature",
                "excerpt": "Speed improves retention, SEO, and conversion rates.",
                "content": "Performance is not a polishing step. It should be a requirement from design to deployment.",
                "tags": "performance,seo,frontend",
            },
        ]

        for payload in posts:
            BlogPost.objects.update_or_create(
                slug=slugify(payload["title"]),
                defaults={
                    **payload,
                    "is_published": True,
                },
            )

        self.stdout.write(self.style.SUCCESS("Successfully seeded services and blog content."))
