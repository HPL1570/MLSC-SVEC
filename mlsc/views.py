from django.shortcuts import render
from .models import *
import pandas as pd
import smtplib
from django.core.mail import send_mail
from django.conf import settings

import os
# Create your views here.
def home(request):
    return render(request, 'index.html')
def team(request):
    return render(request, 'teams.html')
def event(request):
    return render(request, 'events.html')
def blog(request):
    return render(request, 'blogs.html')
def project(request):
    return render(request, 'projects.html')
def registerNE(request):
    return render(request, 'addnew.html')
def registerE(request):
    return render(request, 'register-2.html')

def storeDetails(request):
    if request.method == 'POST':
        fn = request.POST['fulln']
        email = request.POST['email']
        rolln = request.POST['rolln']
        contact = request.POST['contact']
        clgname = request.POST['clgname']
        
        if Registration.objects.filter(rollnumber=rolln).exists() or Registration.objects.filter(email=email).exists():
            print("EMAIL OR ROLLNUMBER ALREADY REGISTERED")
            error_message = 'EMAIL OR ROLLNUMBER ALREADY EXSISTED'
            return render(request, 'index.html', {'error_message': error_message})
        else:
            error_message='YOUR REGISTRATION IS COMPLETED THANK YOU PLEASE CHECK YOUR MAIL FROM MLSC IF NOT FOUND CHECK IN JUNK MAIL'
            obj = Registration.objects.create(name=fn, email=email, rollnumber=rolln, contact_number=contact, college_name=clgname)
            print("Registration")
            obj.save();
            # send_email(request)
            # return render(request, 'index.html', {'error_message': error_message})
    
    return render(request, 'index.html', {'error_message': error_message})
# def sentmail(name,email,rolln,con,clg):
def sendIn(request):
    if request.method == 'POST':
        fn = request.POST['name']
        email = request.POST['mail']
        rolln = request.POST['roll']
        branch = request.POST['branch']
        event = request.POST['event']
        if EventRe.objects.filter(rollnumber=rolln).exists() or EventRe.objects.filter(email=email).exists():
            print("EMAIL OR ROLLNUMBER ALREADY REGISTERED")
            error_message = 'EMAIL OR ROLLNUMBER ALREADY EXSISTED'
            return render(request, 'index.html', {'error_message': error_message})
        else:
            error_message='YOUR REGISTRATION IS COMPLETED THANK YOU PLEASE CHECK YOUR MAIL FROM MLSC IF NOT FOUND CHECK IN JUNK MAIL'
            obj = EventRe.objects.create(name=fn, email=email, rollnumber=rolln,branch=branch,event=event)
            print("Registration")
            sendmail(name=fn, email=email,rollno=rolln,branch=branch,event=event)
            obj.save();
            
    return render(request, 'index.html', {'error_message': error_message})
def sendmail(name=None, email=None, rollno=None,branch=None,event=None):
    subject="Invitation from MLSC-SVEC workshop"
    message=f"""
    Dear {name},

We are excited to invite you to our upcoming web development workshop! This workshop will be a great opportunity for you to enhance your skills and learn about the latest trends in web development.

**Workshop Details:**
- **Date:** March 14, 2024
- **Time:** 10:00 AM IST
- **Location:** Swami Vivekananda Seminar Hall
- **Agenda:** To gain knowledge of the latest trends in web development

**Registration:** Your registration is accepted for {event} !
your details 
Roll number :{rollno}
Branch :{branch}
If you have any questions or need further information, feel free to contact us at coordinator.

We look forward to seeing you at the workshop!

Best regards,
MLSC Team
MLSC SVEC
"""
    from_email= settings.EMAIL_HOST_USER
    receipient=[email]
    send_mail(subject,message,from_email,receipient)