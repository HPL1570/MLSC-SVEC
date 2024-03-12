from django.shortcuts import render
from .models import *
import pandas as pd
import smtplib

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
            send_email(request)
            return render(request, 'index.html', {'error_message': error_message})
    
    return render(request, 'index.html', {'error_message': error_message})
# def sentmail(name,email,rolln,con,clg):
   
