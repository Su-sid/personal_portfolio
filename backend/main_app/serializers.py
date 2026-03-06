from rest_framework import serializers

from .models import (
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


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ("id", "name", "icon")


class ProjectSerializer(serializers.ModelSerializer):
    technologies_used = TechnologySerializer(many=True, read_only=True)
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "description",
            "category",
            "github_link",
            "live_demo_link",
            "is_featured",
            "created_at",
            "technologies_used",
            "image_url",
        )

    def get_image_url(self, obj: Project):
        request = self.context.get("request")
        if not obj.image:
            return None
        return request.build_absolute_uri(obj.image.url) if request else obj.image.url


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = (
            "id",
            "title",
            "summary",
            "description",
            "icon",
            "display_order",
            "is_featured",
        )


class ExperienceSerializer(serializers.ModelSerializer):
    duration = serializers.FloatField(read_only=True)

    class Meta:
        model = Experience
        fields = (
            "id",
            "start_date",
            "end_date",
            "is_current",
            "job_title",
            "company",
            "location",
            "description",
            "duration",
            "is_short",
        )


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = (
            "id",
            "start_date",
            "end_date",
            "institution",
            "location",
            "degree_type",
            "field_of_study",
            "description",
        )


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ("id", "name", "category", "icon")


class ProgrammingLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammingLanguage
        fields = ("id", "name", "icon")


class BlogPostListSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()
    cover_image_url = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = (
            "id",
            "title",
            "slug",
            "excerpt",
            "tags",
            "published_at",
            "created_at",
            "cover_image_url",
        )

    def get_tags(self, obj: BlogPost):
        return obj.tag_list

    def get_cover_image_url(self, obj: BlogPost):
        request = self.context.get("request")
        if not obj.cover_image:
            return None
        return request.build_absolute_uri(obj.cover_image.url) if request else obj.cover_image.url


class BlogPostDetailSerializer(BlogPostListSerializer):
    class Meta(BlogPostListSerializer.Meta):
        fields = BlogPostListSerializer.Meta.fields + ("content", "updated_at")


class ContactInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInquiry
        fields = ("id", "full_name", "email", "message", "created_at")
        read_only_fields = ("id", "created_at")
