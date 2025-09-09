from django.contrib import admin

from main_app.models import Experience,Education,ProgrammingLanguage,Skill,Project

# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category', 'created_at','technologies_used')
    search_fields = ('title', 'description')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company', 'start_date', 'end_date', 'is_current')
    list_filter = ('company', 'start_date')
    search_fields = ('job_title', 'company', 'description')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('institution', 'degree_type', 'field_of_study', 'start_date', 'end_date')
    list_filter = ('institution', 'degree_type')
    search_fields = ('institution', 'field_of_study')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'icon')
    list_filter = ('category',)

@admin.register(ProgrammingLanguage)
class ProgrammingLanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')