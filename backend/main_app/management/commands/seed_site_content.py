from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.text import slugify

from main_app.models import BlogPost, Service

SERVICE_SEEDS = (
    {
        "title": "Website Design & Development",
        "summary": "Conversion-focused websites and product surfaces for modern service businesses.",
        "description": (
            "I design and build websites that are meant to do more than look polished.\n\n"
            "That means structuring pages around decision-making, making content easy to maintain, and keeping the frontend fast "
            "enough to support SEO, conversion, and long-term iteration.\n\n"
            "Typical delivery includes discovery, information architecture, interface implementation, CMS or admin support, and "
            "production deployment."
        ),
        "icon": "i-lucide-layout-template",
        "display_order": 1,
        "is_featured": True,
    },
    {
        "title": "AI & Automation Systems",
        "summary": "Practical AI workflows that reduce repetitive work and improve operational response time.",
        "description": (
            "I build AI-enabled systems with a bias toward constrained, useful workflows rather than novelty demos.\n\n"
            "The focus is usually intake automation, knowledge retrieval, operational assistants, or decision support that fits into "
            "existing team behavior.\n\n"
            "Every implementation is scoped around reliability, observability, and clear handoff points so teams can trust the output."
        ),
        "icon": "i-lucide-bot",
        "display_order": 2,
        "is_featured": True,
    },
    {
        "title": "Technical Strategy & Delivery",
        "summary": "Architecture, scoping, and execution support for teams that need a practical delivery partner.",
        "description": (
            "I help teams turn broad product intentions into a delivery plan that can actually ship.\n\n"
            "That includes technical scoping, implementation tradeoffs, API and data model planning, and reducing the risk that comes "
            "from vague requirements.\n\n"
            "The end result is a clearer path from concept to production, with fewer avoidable rebuilds during execution."
        ),
        "icon": "i-lucide-briefcase-business",
        "display_order": 3,
        "is_featured": True,
    },
)

BLOG_POST_SEEDS = (
    {
        "title": "How I scope delivery before writing code",
        "excerpt": "The fastest way to ship is to remove ambiguity before implementation starts.",
        "content": (
            "Most delivery problems show up long before a repository is opened.\n\n"
            "I start by tightening the scope around goals, user actions, content, integrations, and operational constraints. "
            "That makes tradeoffs visible early and usually cuts rework more than any tooling choice.\n\n"
            "A good scope is specific enough to guide build decisions but flexible enough to survive feedback once users touch the product."
        ),
        "tags": "delivery,planning,product",
    },
    {
        "title": "Adding AI features without overengineering the stack",
        "excerpt": "Useful AI products start with bounded workflows, not maximal orchestration.",
        "content": (
            "The most dependable AI systems are often the least theatrical.\n\n"
            "Instead of reaching for complex multi-agent patterns first, I usually begin with a single narrow workflow, explicit "
            "inputs, and a place for human review when confidence matters.\n\n"
            "That approach keeps failure modes legible and makes it much easier to improve the system once usage data starts coming in."
        ),
        "tags": "ai,engineering,operations",
    },
    {
        "title": "Why performance and clarity are revenue features",
        "excerpt": "A site that loads quickly and explains itself well creates better business conversations.",
        "content": (
            "Performance is not a finishing touch. It changes whether a visitor stays long enough to understand the offer.\n\n"
            "The same is true for interface clarity. If people cannot tell what you do, what to trust, or what to do next, the design "
            "is underperforming regardless of aesthetics.\n\n"
            "Fast pages and clear narrative structure improve conversion because they reduce hesitation at the exact point a prospect "
            "is deciding whether to keep going."
        ),
        "tags": "performance,ux,conversion",
    },
)


class Command(BaseCommand):
    help = "Seed services and blog content that matches the current portfolio frontend."

    def add_arguments(self, parser):
        parser.add_argument(
            "--prune",
            action="store_true",
            help="Delete services and blog posts that are not part of the current seed set.",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        seeded_service_titles = []
        seeded_post_slugs = []

        for payload in SERVICE_SEEDS:
            Service.objects.update_or_create(
                title=payload["title"],
                defaults=payload,
            )
            seeded_service_titles.append(payload["title"])

        for payload in BLOG_POST_SEEDS:
            slug = slugify(payload["title"])
            BlogPost.objects.update_or_create(
                slug=slug,
                defaults={
                    **payload,
                    "is_published": True,
                },
            )
            seeded_post_slugs.append(slug)

        pruned_services = 0
        pruned_posts = 0
        if options["prune"]:
            pruned_services, _ = Service.objects.exclude(
                title__in=seeded_service_titles
            ).delete()
            pruned_posts, _ = BlogPost.objects.exclude(
                slug__in=seeded_post_slugs
            ).delete()

        self.stdout.write(
            self.style.SUCCESS(
                f"Seeded {len(SERVICE_SEEDS)} services and {len(BLOG_POST_SEEDS)} blog posts."
            )
        )
        if options["prune"]:
            self.stdout.write(
                self.style.SUCCESS(
                    f"Pruned {pruned_services} stale services and {pruned_posts} stale blog posts."
                )
            )
