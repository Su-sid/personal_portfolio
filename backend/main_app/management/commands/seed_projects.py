import os
from django.core.management.base import BaseCommand
from django.core.files import File
from django.conf import settings

from main_app.models import Technology, Project

class Command(BaseCommand):
    help = 'Seeds the database with initial project and technology data from David Sudi\'s CV'

    def handle(self, *args, **kwargs):
        # First, clear existing data to avoid duplicates
        Project.objects.all().delete()
        Technology.objects.all().delete()
        
        self.stdout.write("Cleared existing project and technology data.")

        # Create Technologies based on CV
        technologies_to_create = [
            Technology(name='Python', icon='fab fa-python'),
            Technology(name='React', icon='fab fa-react'),
            Technology(name='Next.js', icon='fas fa-code-branch'),
            Technology(name='Redux', icon='fas fa-sync'),
            Technology(name='Jest', icon='fas fa-vial'),
            Technology(name='Cypress', icon='fas fa-flask'),
            Technology(name='LangChain', icon='fas fa-robot'),
            Technology(name='Playwright', icon='fas fa-cogs'),
            Technology(name='HTML/CSS', icon='fab fa-html5'),
            Technology(name='PostgreSQL', icon='fas fa-database'),
            Technology(name='PHP', icon='fab fa-php'),
            Technology(name='Laravel', icon='fab fa-laravel'),
            Technology(name='Git', icon='fab fa-git-alt'),
            Technology(name='GitHub Actions', icon='fas fa-tasks'),
            Technology(name='NLP', icon='fas fa-comments'),
            Technology(name='Data Analysis', icon='fas fa-chart-bar'),
            Technology(name='Machine Learning', icon='fas fa-brain')
        ]
        
        created_technologies = {tech.name: tech for tech in Technology.objects.bulk_create(technologies_to_create)}
        self.stdout.write(self.style.SUCCESS('Successfully created all technologies.'))

        # Create Projects based on CV
        projects_to_create = [
            Project(
                title='Bazar',
                description='An Afro chatbot that processed collected datasets to provide intelligent house and car recommendations for the Bazar website.',
                category='ai',
                is_featured=True
            ),
            Project(
                title='Car Manuals RAG System',
                description='A Retrieval-Augmented Generation (RAG) system for car manuals. This project likely involves implementing text analysis solutions and information extraction from unstructured data, as mentioned in the CV.',
                category='ai',
                is_featured=True
            ),
            Project(
                title='High Risk Taxpayer Prediction Model',
                description='A machine learning model designed to predict high-risk taxpayers. This project demonstrates skills in data analysis, machine learning, and data visualization.',
                category='data',
                is_featured=False
            ),
        ]

        created_projects = Project.objects.bulk_create(projects_to_create)
        self.stdout.write(self.style.SUCCESS('Successfully created all projects.'))
        
        # Add technologies to projects
        project_bazar = Project.objects.get(title='Bazar')
        project_bazar.technologies_used.add(
            created_technologies['Python'],
            created_technologies['LangChain'],
            created_technologies['NLP']
        )
        
        project_car_manuals = Project.objects.get(title='Car Manuals RAG System')
        project_car_manuals.technologies_used.add(
            created_technologies['Python'],
            created_technologies['LangChain'],
            created_technologies['NLP']
        )
        
        project_taxpayer_model = Project.objects.get(title='High Risk Taxpayer Prediction Model')
        project_taxpayer_model.technologies_used.add(
            created_technologies['Python'],
            created_technologies['Machine Learning'],
            created_technologies['Data Analysis']
        )

        self.stdout.write(self.style.SUCCESS('Successfully seeded database with project data from CV.'))