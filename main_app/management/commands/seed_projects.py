import os
from django.core.management.base import BaseCommand
from django.core.files import File
from django.conf import settings

from main_app.models import Technology, Project
# from yourapp.models import Project, Technology  # Replace 'yourapp' with your actual app name

class Command(BaseCommand):
    help = 'Seeds the database with initial project and technology data'

    def handle(self, *args, **kwargs):
        # First, clear existing data to avoid duplicates
        Technology.objects.all().delete()
        Project.objects.all().delete()

        # Create Technologies
        technologies = [
            Technology(name='Python', icon='fab fa-python'),
            Technology(name='Django', icon='fas fa-server'),
            Technology(name='React', icon='fab fa-react'),
            Technology(name='JavaScript', icon='fab fa-js'),
            Technology(name='Docker', icon='fab fa-docker'),
            Technology(name='AWS', icon='fab fa-aws'),
            Technology(name='TensorFlow', icon='fas fa-brain'),
            Technology(name='Node.js', icon='fab fa-node-js')
        ]
        
        # Bulk create technologies
        created_technologies = Technology.objects.bulk_create(technologies)

        # Prepare image path (ensure this matches your project structure)
        image_dir = os.path.join(settings.BASE_DIR, 'seed_images')
        os.makedirs(image_dir, exist_ok=True)

        # Create Projects
        projects = [
            Project(
                title='Intelligent Task Manager',
                description='A full-stack task management application with AI-powered task prioritization and smart scheduling. Features include real-time collaboration, machine learning-based productivity insights, and seamless integration with popular productivity tools.',
                category='web',
                github_link='https://github.com/yourusername/task-manager',
                live_demo_link='https://intelligent-task-manager.herokuapp.com',
                is_featured=True
            ),
            Project(
                title='IoT Home Automation',
                description='A comprehensive IoT solution for smart home management. The system allows users to control and monitor home devices remotely, with features like energy consumption tracking, automated climate control, and security monitoring through a mobile and web interface.',
                category='iot',
                github_link='https://github.com/yourusername/home-automation',
                is_featured=True
            ),
            Project(
                title='E-commerce Recommender Engine',
                description='A machine learning-powered recommendation system for an e-commerce platform. Utilizes collaborative filtering and deep learning algorithms to provide personalized product recommendations, improving user engagement and sales conversion rates.A machine learning-powered recommendation system for an e-commerce platform. Utilizes collaborative filtering and deep learning algorithms to provide personalized product recommendations, improving user engagement and sales conversion rates.',
                category='data',
                github_link='https://github.com/yourusername/ecommerce-recommender',
                live_demo_link='https://product-recommender-demo.netlify.app',
                is_featured=True
            ),
            Project(
                title='Mobile Health Tracking App',
                description='A cross-platform mobile application for comprehensive health and fitness tracking. Features include workout logging, nutrition tracking, heart rate monitoring, sleep analysis, and personalized health recommendations based on user data.',
                category='mobile',
                github_link='https://github.com/yourusername/health-tracker',
                is_featured=False
            )
        ]

        # Create projects
        created_projects = Project.objects.bulk_create(projects)

        # Add technologies to projects
        created_projects[0].technologies_used.add(
            created_technologies[0],  # Python
            created_technologies[1],  # Django
            created_technologies[3],  # JavaScript
            created_technologies[4]   # Docker
        )
        created_projects[1].technologies_used.add(
            created_technologies[0],  # Python
            created_technologies[5],  # AWS
            created_technologies[6]   # TensorFlow
        )
        created_projects[2].technologies_used.add(
            created_technologies[0],  # Python
            created_technologies[6],  # TensorFlow
            created_technologies[3],  # JavaScript
            created_technologies[7]   # Node.js
        )
        created_projects[3].technologies_used.add(
            created_technologies[2],  # React
            created_technologies[3],  # JavaScript
            created_technologies[7]   # Node.js
        )

        # Optional: Add images (commented out, as you'll need to provide actual images)
        # for project in created_projects:
        #     image_path = os.path.join(image_dir, f'{project.title.lower().replace(" ", "_")}.jpg')
        #     if os.path.exists(image_path):
        #         with open(image_path, 'rb') as image_file:
        #             project.image.save(
        #                 os.path.basename(image_path), 
        #                 File(image_file), 
        #                 save=True
        #             )

        self.stdout.write(self.style.SUCCESS('Successfully seeded database with project data'))