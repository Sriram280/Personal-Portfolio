from django.shortcuts import render, redirect
from django.contrib import messages

from .models import (
    Skill,
    Project,
    Education,
    Experience,
    Contact,
)


def home(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        if name and email and message:

            Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )

            messages.success(
                request,
                "Your message has been sent successfully!"
            )

            return redirect("home")

        messages.error(
            request,
            "Please fill in all required fields."
        )

    context = {
        "skills": Skill.objects.all(),
        "projects": Project.objects.all(),
        "education": Education.objects.all(),
        "experience": Experience.objects.all(),
    }

    return render(request, "main/index.html", context)