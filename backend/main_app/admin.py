from django.contrib import admin

from main_app.models import (
    BlogPost,
    ContactInquiry,
    Project,
    Service,
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


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ("name", "icon")
    search_fields = ("name",)
