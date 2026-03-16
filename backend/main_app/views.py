from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from main_app.forms import ContactForm
from main_app.viewsmodels import ProjectViewModel


def index(request):

    return render(request, "index.html")


@require_http_methods(["GET", "POST"])
def contact(request):
    form = ContactForm(request.POST or None)

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Add a success message
            messages.success(request, "Your message has been sent successfully!")

            # Redirect to prevent form resubmission
            return redirect("contacts")

    return render(request, "contact.html", {"form": form})


@require_http_methods(["GET"])
def projects(request):
    # Get projects data from viewmodel
    context = ProjectViewModel.get_projects()
    return render(request, "projects.html", context)
