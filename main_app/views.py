from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse

from main_app.forms import ContactForm
from main_app.viewsmodels import ProjectViewModel, ResumeViewModel

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
    # Get projects data from viewmodel
    context = ProjectViewModel.get_projects()
    return render(request, 'projects.html', context)


@require_http_methods(["GET"])
def resume(request):
    """
    Render the resume page with all dynamic content
    """
    context = ResumeViewModel.get_resume_data()
    return render(request, 'resume.html', context)