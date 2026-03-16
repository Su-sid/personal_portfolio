from django.db import DatabaseError
from typing import Any, Dict, List

from .models import Project


class BaseViewModel:
    @staticmethod
    def get_error_message() -> str:
        """Get the standard error message for database errors"""
        return "Unable to connect to the database. Please try again later."

    @classmethod
    def update_state(
        cls, initial_state: Dict[str, Any], db_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Update initial state with database values if available"""
        try:
            return {**initial_state, **db_data}
        except Exception:
            return {**initial_state, "error": cls.get_error_message()}


class ProjectViewModel(BaseViewModel):
    # Initial state with empty lists
    initial_state = {"featured_projects": [], "all_projects": []}

    @classmethod
    def get_projects(cls) -> Dict[str, List[Project]]:
        """Get projects with fallback to initial state"""
        try:
            db_data = {
                "featured_projects": list(Project.objects.filter(is_featured=True)),
                "all_projects": list(Project.objects.all()),
            }
            return cls.update_state(cls.initial_state, db_data)
        except DatabaseError:
            return {**cls.initial_state, "error": cls.get_error_message()}
