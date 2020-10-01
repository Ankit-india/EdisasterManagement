from django.shortcuts import redirect
from .models import Feedback


def feedback(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        feedback = Feedback(name=name, email=email, subject=subject, message=message)
        feedback.save()
        return redirect('/')