from django.db import models
from django.utils import timezone
from django.utils.text import Truncator


class Technology(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, help_text="Bootstrap icon class")

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Project(models.Model):
    CATEGORY_CHOICES = [
        ("web", "Web Development"),
        ("mobile", "Mobile App"),
        ("data", "Data Science"),
        ("ai", "AI Engineering"),
        ("prompting", "Prompt Engineering"),
        ("iot", "Internet of Things"),
        ("other", "Other"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(
        upload_to="project_images/",
        null=True,
        blank=True,
        help_text="Upload project image (recommended 1200x800)",
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="other")
    github_link = models.URLField(null=True, blank=True)
    live_demo_link = models.URLField(null=True, blank=True)
    technologies_used = models.ManyToManyField("Technology", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def description_preview(self) -> str:
        return Truncator(self.description).words(30)

    def __str__(self) -> str:
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=120)
    summary = models.CharField(max_length=220)
    description = models.TextField()
    icon = models.CharField(max_length=50, default="bi-gear")
    display_order = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order", "title"]

    def __str__(self) -> str:
        return self.title


class Experience(models.Model):
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        ordering = ["-start_date"]
        verbose_name_plural = "Experiences"

    @property
    def duration(self) -> float:
        end_date = timezone.now().date() if self.is_current else self.end_date
        if not end_date:
            return 0
        duration_years = (end_date.year - self.start_date.year) + (end_date.month - self.start_date.month) / 12.0
        return duration_years

    @property
    def is_short(self) -> bool:
        return self.duration < 1

    def __str__(self) -> str:
        return f"{self.job_title} @ {self.company}"


class Education(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    institution = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    degree_type = models.CharField(max_length=50)
    field_of_study = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["-start_date"]
        verbose_name_plural = "Education Entries"

    def __str__(self) -> str:
        return f"{self.degree_type} in {self.field_of_study} from {self.institution}"


class Skill(models.Model):
    SKILL_CATEGORIES = [
        ("PROFESSIONAL", "Professional Skills"),
        ("TECHNICAL", "Technical Skills"),
        ("SOFT", "Soft Skills"),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=SKILL_CATEGORIES)
    icon = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Bootstrap icon class (e.g., 'bi-tools')",
    )

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Bootstrap icon class (e.g., 'bi-code-slash')",
    )

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    excerpt = models.CharField(max_length=300)
    content = models.TextField()
    cover_image = models.ImageField(upload_to="blog_covers/", null=True, blank=True)
    tags = models.CharField(max_length=300, blank=True, help_text="Comma-separated tags")
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-published_at", "-created_at"]

    def save(self, *args, **kwargs):
        if self.is_published and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    @property
    def tag_list(self) -> list[str]:
        return [tag.strip() for tag in self.tags.split(",") if tag.strip()]

    def __str__(self) -> str:
        return self.title


class ContactInquiry(models.Model):
    full_name = models.CharField(max_length=70)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    responded = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Contact Inquiries"

    def __str__(self) -> str:
        return f"{self.full_name} <{self.email}>"
