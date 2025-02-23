from django.shortcuts import render
from .forms import ApplicationForm
from django.contrib import messages
from django.core.mail import EmailMessage

def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save()  # ✅ Save the form once (prevents duplicates)

            # Email confirmation
            message_body = f"A new job application was submitted. Thank you, {application.first_name} {application.last_name}."
            email_message = EmailMessage("Form submission confirmation", message_body, to=[application.email])
            email_message.send()

            messages.success(request, "Form submitted successfully")
        else:
            messages.error(request, "Error submitting form. Please check your inputs.")

    else:
        form = ApplicationForm()

    return render(request, "index.html", {"form": form})

def about(request):
    return render(request, "about.html")



