from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods
# Create your views here.
from django.http import HttpResponse

from main_app.forms import ContactForm
from main_app.models import Education, Experience, ProgrammingLanguage, Project, Skill

def index(request):
  
    return render(request, 'index.html')


@require_http_methods(["GET", "POST"])
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Add a success message
            messages.success(request, 'Your message has been sent successfully!')
            
            # Redirect to prevent form resubmission
            return redirect('contacts')  
    elif request.method== "GET":
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})

@require_http_methods(["GET"])
def projects(request):
    # Get featured projects first, then all projects
    featured_projects = Project.objects.filter(is_featured=True)
    all_projects = Project.objects.all()

    context = {
        'featured_projects': featured_projects,
        'all_projects': all_projects
    }
    return render(request, 'projects.html', context)


@require_http_methods(["GET"])
def resume(request):
    """
    Render the resume page with all dynamic content
    """
    experiences = Experience.objects.all()

    # Separate experiences into long and short in Python
    long_experiences = [exp for exp in experiences if not exp.is_short]  # Long experiences
    short_experiences = [exp for exp in experiences if exp.is_short]  # Short experiences

    # Get all education entries, ordered by most recent first
    education_entries = Education.objects.all()

    # Get professional skills
    professional_skills = Skill.objects.filter(category='PROFESSIONAL')

    # Get programming languages
    programming_languages = ProgrammingLanguage.objects.all()

    context = {
        'long_experiences': sorted(long_experiences, key=lambda x: x.duration, reverse=True),
        'short_experiences': sorted(short_experiences, key=lambda x: x.duration, reverse=True),
        'education_entries': education_entries,
        'professional_skills': professional_skills,
        'programming_languages': programming_languages,
    }

    return render(request, 'resume.html', context)