from django.core.management.base import BaseCommand
from django.db import transaction

from main_app.models import Project, Technology

TECHNOLOGY_SEEDS = {
    "Nuxt": {"icon": "bi-lightning-charge"},
    "Vue": {"icon": "bi-code-slash"},
    "Django": {"icon": "bi-grid-3x3-gap"},
    "Python": {"icon": "bi-filetype-py"},
    "PostgreSQL": {"icon": "bi-database"},
    "Docker": {"icon": "bi-box-seam"},
    "GitHub Actions": {"icon": "bi-github"},
    "LangChain": {"icon": "bi-bezier2"},
    "OpenAI API": {"icon": "bi-stars"},
    "FastAPI": {"icon": "bi-diagram-3"},
    "Pandas": {"icon": "bi-bar-chart"},
    "SQL": {"icon": "bi-database-gear"},
}

PROJECT_SEEDS = (
    {
        "title": "Portfolio Platform",
        "description": (
            "A full-stack portfolio platform that pairs a Nuxt SSR frontend with a Django API and admin workflow.\n\n"
            "The product is structured around services, case studies, writing, and direct inquiry capture so the public site and "
            "the content model stay aligned.\n\n"
            "Deployment is containerized with Docker Compose, which keeps the production stack predictable and makes CI/CD into "
            "Coolify straightforward."
        ),
        "category": "web",
        "is_featured": True,
        "github_link": None,
        "live_demo_link": None,
        "technologies": (
            "Nuxt",
            "Vue",
            "Django",
            "Python",
            "PostgreSQL",
            "Docker",
            "GitHub Actions",
        ),
    },
    {
        "title": "AI Workflow Assistant",
        "description": (
            "An AI-assisted operations workflow built to turn messy project requests into structured next actions.\n\n"
            "The system combines prompt-driven extraction, validation, and routing so delivery teams can respond faster without "
            "introducing opaque automation.\n\n"
            "The implementation favors constrained workflows, review checkpoints, and observable outputs instead of trying to "
            "hide the decision process behind a single model call."
        ),
        "category": "ai",
        "is_featured": True,
        "github_link": None,
        "live_demo_link": None,
        "technologies": (
            "Python",
            "LangChain",
            "OpenAI API",
            "FastAPI",
            "PostgreSQL",
            "Docker",
        ),
    },
    {
        "title": "Delivery Reporting Workspace",
        "description": (
            "A reporting workspace for surfacing delivery health, commercial signals, and operational bottlenecks in one place.\n\n"
            "It consolidates project data into readable summaries for founders and stakeholders, with an emphasis on trend visibility "
            "instead of dashboard noise.\n\n"
            "The result is a lightweight analytics layer that supports better planning conversations without adding heavy process."
        ),
        "category": "data",
        "is_featured": True,
        "github_link": None,
        "live_demo_link": None,
        "technologies": (
            "Python",
            "Pandas",
            "SQL",
            "PostgreSQL",
            "Docker",
        ),
    },
)


class Command(BaseCommand):
    help = "Seed featured projects and supporting technologies for the current portfolio frontend."

    def add_arguments(self, parser):
        parser.add_argument(
            "--prune",
            action="store_true",
            help="Delete projects that are not part of the current seed set.",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        seeded_titles = []
        technology_map = {}

        for name, defaults in TECHNOLOGY_SEEDS.items():
            technology, _ = Technology.objects.update_or_create(
                name=name,
                defaults=defaults,
            )
            technology_map[name] = technology

        for payload in PROJECT_SEEDS:
            project, _ = Project.objects.update_or_create(
                title=payload["title"],
                defaults={
                    "description": payload["description"],
                    "category": payload["category"],
                    "is_featured": payload["is_featured"],
                    "github_link": payload["github_link"],
                    "live_demo_link": payload["live_demo_link"],
                },
            )
            project.technologies_used.set(
                [technology_map[name] for name in payload["technologies"]]
            )
            seeded_titles.append(project.title)

        pruned_count = 0
        if options["prune"]:
            pruned_count, _ = Project.objects.exclude(title__in=seeded_titles).delete()

        self.stdout.write(
            self.style.SUCCESS(
                f"Seeded {len(PROJECT_SEEDS)} projects and {len(TECHNOLOGY_SEEDS)} technologies."
            )
        )
        if options["prune"]:
            self.stdout.write(
                self.style.SUCCESS(f"Pruned {pruned_count} stale projects.")
            )
