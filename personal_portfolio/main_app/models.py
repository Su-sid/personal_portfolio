from django.db import models
from django.utils import timezone

# Create your models here.

from django.utils.text import Truncator

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('web', 'Web Development'),
        ('mobile', 'Mobile App'),
        ('data', 'Data Science'),
        ('prompting', 'Prompt Engineering'),
        ('iot', 'Internet of Things'),
        ('other', 'Other')
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(
        upload_to='media/project_images/', 
        null=True, 
        blank=True, 
        help_text="Upload project image (recommended 300x300)"
    )
    category = models.CharField(
        max_length=20, 
        choices=CATEGORY_CHOICES, 
        default='other'
    )
    github_link = models.URLField(null=True, blank=True)
    live_demo_link = models.URLField(null=True, blank=True)
    technologies_used = models.ManyToManyField(
        'Technology', 
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)

    def description_preview(self):
        """
        Returns a truncated description for preview
        """
        return Truncator(self.description).words(30)

    def __str__(self):
        return self.title

class Technology(models.Model):

    name = models.CharField(max_length=100)
    icon = models.CharField(
        max_length=50, 
        help_text="Bootstrap icon class"
    )

    def __str__(self):
        return self.name
    

class Experience(models.Model):
    """Model for professional work experience entries"""
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  # Allow for current job
    is_current = models.BooleanField(default=False)
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()

  
    @property
    def duration(self):
        """Calculate the duration of the experience in years."""
        if self.is_current:
            end_date = timezone.now().date()
        else:
            end_date = self.end_date
        
        duration_years = (end_date.year - self.start_date.year) + \
                         (end_date.month - self.start_date.month) / 12.0
        return duration_years

    @property
    def is_short(self):
        """Determine if the experience is less than a year."""
        return self.duration < 1
    
    class Meta:
        ordering = ['-start_date']
        verbose_name_plural = "Experiences"

class Education(models.Model):
    """Model for educational background entries"""
    start_date = models.DateField()
    end_date = models.DateField()
    institution = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    degree_type = models.CharField(max_length=50)  # e.g., "Undergraduate", "Master's"
    field_of_study = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.degree_type} in {self.field_of_study} from {self.institution}"
    
    class Meta:
        ordering = ['-start_date']
        verbose_name_plural = "Education Entries"

class Skill(models.Model):
    """Model for professional skills with Bootstrap icon support"""
    SKILL_CATEGORIES = [
        ('PROFESSIONAL', 'Professional Skills'),
        ('TECHNICAL', 'Technical Skills'),
        ('SOFT', 'Soft Skills')
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=SKILL_CATEGORIES)
    # Bootstrap icon class for visual representation
    icon = models.CharField(
        max_length=50, 
        blank=True, 
        null=True, 
        help_text="Bootstrap icon class (e.g., 'bi-tools')"
    )
    
    def __str__(self):
        return self.name

class ProgrammingLanguage(models.Model):
    """Model for programming languages and technologies with Bootstrap icon support"""
    name = models.CharField(max_length=50)
    # Bootstrap icon class for visual representation
    icon = models.CharField(
        max_length=50, 
        blank=True, 
        null=True, 
        help_text="Bootstrap icon class (e.g., 'bi-code-slash')"
    )
    
    def __str__(self):
        return self.name
