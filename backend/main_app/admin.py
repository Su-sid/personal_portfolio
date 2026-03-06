from django.contrib import admin

from main_app.models import (
    BlogPost,
    ContactInquiry,
    Education,
    Experience,
    ProgrammingLanguage,
    Project,
    Service,
    Skill,
    Technology,
)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_featured", "created_at")
    list_filter = ("category", "is_featured", "created_at")
    search_fields = ("title", "description")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "display_order", "is_featured")
    list_filter = ("is_featured",)
    search_fields = ("title", "summary", "description")
    ordering = ("display_order",)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "is_published", "published_at", "updated_at")
    list_filter = ("is_published", "published_at")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "excerpt", "content", "tags")


@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "responded", "created_at")
    list_filter = ("responded", "created_at")
    search_fields = ("full_name", "email", "message")


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("job_title", "company", "start_date", "end_date", "is_current")
    list_filter = ("company", "start_date")
    search_fields = ("job_title", "company", "description")


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("institution", "degree_type", "field_of_study", "start_date", "end_date")
    list_filter = ("institution", "degree_type")
    search_fields = ("institution", "field_of_study")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "icon")
    list_filter = ("category",)


@admin.register(ProgrammingLanguage)
class ProgrammingLanguageAdmin(admin.ModelAdmin):
    list_display = ("name", "icon")


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ("name", "icon")
    search_fields = ("name",)
