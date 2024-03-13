from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import *

def home(request):
    return render(request, 'index.html')

def sendIn(request):
    if request.method == 'POST':
        fn = request.POST['name']
        email = request.POST['mail']
        rolln = request.POST['roll']
        branch = request.POST['branch']
        event = request.POST['event']

        if EventRe.objects.filter(rollnumber=rolln).exists() or EventRe.objects.filter(email=email).exists():
            print("EMAIL OR ROLLNUMBER ALREADY REGISTERED")
            error_message = 'EMAIL OR ROLLNUMBER ALREADY EXISTED'
            return render(request, 'index.html', {'error_message': error_message})
        else:
            error_message = 'YOUR REGISTRATION IS COMPLETED THANK YOU. PLEASE CHECK YOUR MAIL FROM MLSC. IF NOT FOUND, CHECK IN JUNK MAIL'
            obj = EventRe.objects.create(name=fn, email=email, rollnumber=rolln, branch=branch, event=event)
            print("Registration")
            sendmail(name=fn, email=email, rollno=rolln, branch=branch, event=event)
            obj.save()

    return render(request, 'index.html', {'error_message': error_message})

def sendmail(name=None, email=None, rollno=None, branch=None, event=None):
    subject = "Invitation from MLSC-SVEC workshop"
    html_message = render_to_string('email.html', {'name': name, 'rollno': rollno, 'branch': branch, 'event': event})
    plain_message = strip_tags(html_message)
    from_email = settings.EMAIL_HOST_USER
    recipient = [email]
    
    send_mail(subject, plain_message, from_email, recipient, html_message=html_message)
