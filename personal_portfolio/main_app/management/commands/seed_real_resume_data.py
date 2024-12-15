from django.core.management.base import BaseCommand
from main_app.models import Experience, Education, Skill, ProgrammingLanguage
from datetime import datetime

class Command(BaseCommand):
    help = 'Seeds the database with David Sudi\'s resume data'
    
    def handle(self, *args, **kwargs):
        # Clear existing data (optional)
        Experience.objects.all().delete()
        Education.objects.all().delete()
        Skill.objects.all().delete()
        ProgrammingLanguage.objects.all().delete()
        
        # Create Experiences
        experiences = [
            {
                'start_date': '2024-08-01',
                'end_date': '2024-09-30',
                'is_current': False,
                'job_title': '.NET Junior Developer',
                'company': 'Leizam Ventures',
                'location': 'Nairobi County, Kenya',
                'description': 'Collaborated with cross-functional team to develop web solutions using C# and .NET Framework. Contributed to ERP and terminal applications supporting USSD systems.'
            },
            {
                'start_date': '2024-01-01',
                'end_date': '2024-09-30',
                'is_current': False,
                'job_title': 'DSA and Software Engineering Trainee',
                'company': 'A2SV | Africa to Silicon Valley',
                'location': 'Ethiopia',
                'description': 'Collaborated with developers from African countries to improve competitive programming, data structures, and problem-solving skills.'
            },
            {
                'start_date': '2023-10-01',
                'end_date': '2024-03-31',
                'is_current': False,
                'job_title': 'Python Engineer',
                'company': 'Scale AI',
                'location': 'Remote',
                'description': 'Developed and refined AI models. Performed response evaluation, data analysis, and quality assurance to improve model performance and reliability.'
            },
            {
                'start_date': '2023-01-01',
                'end_date': '2023-04-30',
                'is_current': False,
                'job_title': 'Information Technology Specialist',
                'company': 'County Government of Nakuru',
                'location': 'Nakuru, Kenya',
                'description': 'Conducted network support, implemented VMware, performed system maintenance, managed Windows Server environment, utilized MS SQL, provided technical support, and managed intern team.'
            },
            {
                'start_date': '2021-01-01',
                'end_date': '2022-03-31',
                'is_current': False,
                'job_title': 'Technical Writer',
                'company': 'Cloudzilla.ai',
                'location': 'Remote',
                'description': 'Wrote technical articles on web development, networking, and systems troubleshooting, becoming a reference point for industry best practices.'
            }
        ]
        for exp_data in experiences:
            Experience.objects.create(**exp_data)
        
        # Create Education Entries
        educations = [
            {
                'start_date': '2018-09-01',
                'end_date': '2024-06-30',
                'institution': 'Jomo Kenyatta University of Agriculture and Technology',
                'location': 'Kenya',
                'degree_type': "Bachelor's",
                'field_of_study': 'Computer Technology',
                'description': "I completed a 4-year Bachelor's degree in Computer Technology from the School of Information and Computing (SCIT) at JKUAT, which provided a comprehensive foundation in both hardware and software systems. This program allowed me to develop an integrated understanding of computing, bridging theoretical knowledge with practical skills in software development, data communications, and electronic systems design. Throughout the course, I acquired key technical skills in programming languages, microprocessor design, and system integration, complemented by critical soft skills such as problem-solving, analytical thinking, and adaptability to emerging technologies."
            }
        ]
        for edu_data in educations:
            Education.objects.create(**edu_data)
        
        # Create Skills
        professional_skills = [
            {'name': 'Data Analysis', 'category': 'PROFESSIONAL', 'icon': 'bi-graph-up'},
            {'name': 'Software Quality Assurance', 'category': 'PROFESSIONAL', 'icon': 'bi-shield-check'},
            {'name': 'Prompt Engineering', 'category': 'PROFESSIONAL', 'icon': 'bi-chat-dots'},
            {'name': 'Competitive Programming', 'category': 'PROFESSIONAL', 'icon': 'bi-trophy'},
            {'name': 'Technical Writing', 'category': 'PROFESSIONAL', 'icon': 'bi-pencil-square'},
            {'name': 'Network Support', 'category': 'PROFESSIONAL', 'icon': 'bi-router'}
        ]
        for skill_data in professional_skills:
            Skill.objects.create(**skill_data)
        
        # Create Programming Languages and Technologies
        languages = [
            {'name': 'Python', 'icon': 'bi-python'},
            {'name': 'C#', 'icon': 'bi-hash'},
            {'name': '.NET', 'icon': 'bi-code-slash'},
            {'name': 'MS SQL', 'icon': 'bi-database'},
            {'name': 'VMware', 'icon': 'bi-display'},
            {'name': 'Windows Server', 'icon': 'bi-windows'}
        ]
        for lang_data in languages:
            ProgrammingLanguage.objects.create(**lang_data)
        
        # Create Certifications
        certifications = [
            {'name': 'DevNet Associate', 'issuer': 'Cisco'},
            {'name': 'Fundamentals of Accelerated Computing with CUDA C/C++', 'issuer': 'NVIDIA'}
        ]
        # Note: You might need to create a Certification model if not already existing
        
        self.stdout.write(self.style.SUCCESS('Successfully seeded David Sudi\'s resume data'))