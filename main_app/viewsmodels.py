from django.db import DatabaseError
from typing import Dict, List, Any

from .models import Education, Experience, ProgrammingLanguage, Project, Skill

class BaseViewModel:
    @staticmethod
    def get_error_message() -> str:
        """Get the standard error message for database errors"""
        return "Unable to connect to the database. Please try again later."
        
    @classmethod
    def update_state(cls, initial_state: Dict[str, Any], db_data: Dict[str, Any]) -> Dict[str, Any]:
        """Update initial state with database values if available"""
        try:
            return {**initial_state, **db_data}
        except Exception:
            return {**initial_state, 'error': cls.get_error_message()}

class ProjectViewModel(BaseViewModel):
    # Initial state with empty lists
    initial_state = {
        'featured_projects': [],
        'all_projects': []
    }
    
    @classmethod
    def get_projects(cls) -> Dict[str, List[Project]]:
        """Get projects with fallback to initial state"""
        try:
            db_data = {
                'featured_projects': list(Project.objects.filter(is_featured=True)),
                'all_projects': list(Project.objects.all())
            }
            return cls.update_state(cls.initial_state, db_data)
        except DatabaseError:
            return {**cls.initial_state, 'error': cls.get_error_message()}

class ResumeViewModel(BaseViewModel):
    # Initial state with empty lists for all resume data
    initial_state = {
        'long_experiences': [],
        'short_experiences': [],
        'education_entries': [],
        'professional_skills': [],
        'programming_languages': []
    }
    
    @classmethod
    def get_resume_data(cls) -> Dict[str, Any]:
        """Get resume data with fallback to initial state"""
        try:
            experiences = list(Experience.objects.all())
            db_data = {
                'long_experiences': sorted(
                    [exp for exp in experiences if not exp.is_short],
                    key=lambda x: x.duration,
                    reverse=True
                ),
                'short_experiences': sorted(
                    [exp for exp in experiences if exp.is_short],
                    key=lambda x: x.duration,
                    reverse=True
                ),
                'education_entries': list(Education.objects.all()),
                'professional_skills': list(Skill.objects.filter(category='PROFESSIONAL')),
                'programming_languages': list(ProgrammingLanguage.objects.all())
            }
            return cls.update_state(cls.initial_state, db_data)
        except DatabaseError:
            return {**cls.initial_state, 'error': cls.get_error_message()}
