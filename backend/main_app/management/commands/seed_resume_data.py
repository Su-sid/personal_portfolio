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
        
        # Create Experiences from the CV
        experiences = [
            {
                'start_date': '2024-01-01',
                'end_date': '2025-12-31', 
                'is_current': True, # As of Sept 2025, this role is ongoing.
                'job_title': 'Software Developer',
                'company': 'A2SV Africa to Silicon Valley',
                'location': 'Remote',
                'description': 'Developed client-side applications using React, Redux, and Next.js. Architected Python-based data collection systems with LangChain and Playwright. Executed comprehensive testing strategies including unit, component, and end-to-end testing.'
            },
            {
                'start_date': '2024-01-01',
                'end_date': '2024-12-31',
                'is_current': False,
                'job_title': 'Frontend Developer',
                'company': 'Leizam Ventures',
                'location': 'Nairobi, Kenya',
                'description': 'Maintained technical support for AI-enhanced ERP systems in financial and retail sectors, focusing on data integration and automated reporting features. Collaborated with development teams to implement machine learning features in mobile applications.'
            },
            {
                'start_date': '2023-01-01',
                'end_date': '2023-05-31',
                'is_current': False,
                'job_title': 'Information Technology Assistant',
                'company': 'County Government of Nakuru',
                'location': 'Nakuru, Kenya',
                'description': 'Administered data systems and server environments, implementing monitoring solutions that improved system efficiency by 20%. Facilitated technical training sessions for ICT departments.'
            }
        ]
        for exp_data in experiences:
            Experience.objects.create(**exp_data)
        
        # Create Education Entries from the CV
        educations = [
            {
                'start_date': '2019-09-01', # Assuming start of academic year for '2019'
                'end_date': '2024-05-31', # Assuming end of academic year for '2024'
                'institution': 'Jomo Kenyatta University of Agriculture and Technology',
                'location': 'Kenya',
                'degree_type': "Bachelor's Degree",
                'field_of_study': 'Computer Technology',
                'description': 'Relevant Coursework: Artificial Intelligence, Data Science, Machine Learning, Environmental Informatics, and System Design and Development.'
            }
        ]
        for edu_data in educations:
            Education.objects.create(**edu_data)
        
        # Create Skills from the CV
        professional_skills = [
            {'name': 'AI & Machine Learning', 'category': 'PROFESSIONAL', 'icon': 'bi-robot'},
            {'name': 'Natural Language Processing', 'category': 'PROFESSIONAL', 'icon': 'bi-chat-dots'},
            {'name': 'Data Analysis', 'category': 'PROFESSIONAL', 'icon': 'bi-graph-up'},
            {'name': 'Comprehensive Testing', 'category': 'PROFESSIONAL', 'icon': 'bi-shield-check'},
            {'name': 'Technical Documentation', 'category': 'PROFESSIONAL', 'icon': 'bi-pencil-square'},
            {'name': 'Stakeholder Collaboration', 'category': 'PROFESSIONAL', 'icon': 'bi-people'}
        ]
        for skill_data in professional_skills:
            Skill.objects.create(**skill_data)
        
        # Create Programming Languages and Technologies from the CV
        languages = [
            {'name': 'Python', 'icon': 'bi-python'},
            {'name': 'React', 'icon': 'bi-code-slash'},
            {'name': 'Next.js', 'icon': 'bi-code-slash'},
            {'name': 'Jest', 'icon': 'bi-eyedropper'},
            {'name': 'Cypress', 'icon': 'bi-check2-circle'},
            {'name': 'Playwright', 'icon': 'bi-joystick'},
            {'name': 'PostgreSQL', 'icon': 'bi-database'},
            {'name': 'Microsoft SQL Server', 'icon': 'bi-database-fill'},
            {'name': 'GitHub Actions', 'icon': 'bi-github'},
            {'name': 'Laravel', 'icon': 'bi-code-square'}
        ]
        for lang_data in languages:
            ProgrammingLanguage.objects.create(**lang_data)
        
        # Create Certifications from the CV
        # certifications = [
        #     {'name': 'DevNet Associate', 'issuer': 'Cisco'},
        #     {'name': 'Developing LLM Applications with LangChain', 'issuer': 'DataCamp'},
        #     {'name': 'Fundamentals of Accelerated Computing with CUDA C/C++', 'issuer': 'NVIDIA'}
        # ]
        # Note: You might need to create a Certification model if not already existing.
        # for cert_data in certifications:
        #     Certification.objects.create(**cert_data)
        
        self.stdout.write(self.style.SUCCESS('Successfully seeded David Sudi\'s resume data from the CV'))