
from django.core.management.base import BaseCommand

from main_app.models import Experience,Education, Skill, ProgrammingLanguage


class Command(BaseCommand):
    help = 'Seeds the database with initial resume data'

    def handle(self, *args, **kwargs):
        # Clear existing data (optional)
        Experience.objects.all().delete()
        Education.objects.all().delete()
        Skill.objects.all().delete()
        ProgrammingLanguage.objects.all().delete()

        # Create Experiences
        experiences = [
            {
                'start_date': '2019-01-01',
                'end_date': None,
                'is_current': True,
                'job_title': 'Web Developer',
                'company': 'Stark Industries',
                'location': 'Los Angeles, CA',
                'description': 'Developed and maintained web applications using modern web technologies.'
            },
            {
                'start_date': '2017-06-01',
                'end_date': '2019-12-31',
                'is_current': False,
                'job_title': 'SEM Specialist',
                'company': 'Wayne Enterprises',
                'location': 'Gotham City, NY',
                'description': 'Managed search engine marketing strategies and optimized digital marketing campaigns.'
            }
        ]

        for exp_data in experiences:
            Experience.objects.create(**exp_data)

        # Create Education Entries
        educations = [
            {
                'start_date': '2015-09-01',
                'end_date': '2017-05-30',
                'institution': 'Barnett College',
                'location': 'Fairfield, NY',
                'degree_type': "Master's",
                'field_of_study': 'Web Development',
                'description': 'Advanced studies in web development and modern technologies.'
            },
            {
                'start_date': '2011-09-01',
                'end_date': '2015-05-30',
                'institution': 'ULA',
                'location': 'Los Angeles, CA',
                'degree_type': 'Undergraduate',
                'field_of_study': 'Computer Science',
                'description': 'Comprehensive computer science program with focus on software development.'
            }
        ]

        for edu_data in educations:
            Education.objects.create(**edu_data)

        # Create Skills
        professional_skills = [
            {'name': 'SEO Optimization', 'category': 'PROFESSIONAL', 'icon': 'bi-tools'},
            {'name': 'Statistical Analysis', 'category': 'PROFESSIONAL', 'icon': 'bi-tools'},
            {'name': 'Web Development', 'category': 'PROFESSIONAL', 'icon': 'bi-tools'},
            {'name': 'Prompting', 'category': 'PROFESSIONAL', 'icon': 'bi-chat-dots'},
            {'name': 'Adobe Software Suite', 'category': 'PROFESSIONAL', 'icon': 'bi-tools'},
            {'name': 'User Interface Design', 'category': 'PROFESSIONAL', 'icon': 'bi-tools'}
        ]

        for skill_data in professional_skills:
            Skill.objects.create(**skill_data)

        # Create Programming Languages
        languages = [
            {'name': 'HTML', 'icon': 'bi-code-square'},
            {'name': 'CSS', 'icon': 'bi-palette'},
            {'name': 'JavaScript', 'icon': 'bi-js-square'},
            {'name': 'Python', 'icon': 'bi-python'},
            {'name': 'C#', 'icon': 'bi-hash'},
            {'name': 'Django', 'icon': 'bi-code-slash'}
        ]

        for lang_data in languages:
            ProgrammingLanguage.objects.create(**lang_data)

        self.stdout.write(self.style.SUCCESS('Successfully seeded resume data'))