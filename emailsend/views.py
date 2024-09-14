from django.shortcuts import render,get_object_or_404,redirect
from django.core.mail import EmailMessage
from .models import *
import datetime
import requests

def send_email_view(request):
    if request.method == 'POST':
        roll_no = request.POST.get("roll_number")
        user_object = get_object_or_404(students, roll_no=roll_no)
        parent_mail_1, parent_mail_2, is_inside_1 = user_object.parents_mail_1, user_object.parents_mail_2, user_object.is_inside
        time = datetime.datetime.now()
        if is_inside_1:
            sub = f"Your Son/Daughter has gone outside to off campus at {time}"
            user_object.is_inside = False
        else:
            sub = f"Your Son/Daughter has gone inside to campus at {time}"
            user_object.is_inside = True  # set to inside
        user_object.save()
        email = EmailMessage('Test Email from Django',sub,'erodesengunthar0@gmail.com',[parent_mail_1, parent_mail_2],)
        email.fail_silently = False
        try:
            email.send()
            return render(request, "index.html",{"message":"Email Sent Successful","name":user_object.name})
        except Exception as e:
            return render(request, "index.html",{"message":f"Error sending email:{str(e)}"})
    else:
        return render(request, "index.html")

def checkinside(request):
    if request.method == 'POST':
        roll_no = request.POST.get("roll_number")
        user_object = get_object_or_404(students, roll_no=roll_no)
        if user_object.is_inside:
            sub = f"Your Son/Daughter is inside the campus"
        else:
            sub = f"Your Son/Daughter is gone outside the campus"
        return render(request, "index.html",{"message":sub,"name":user_object.name})
    return render(request, "index.html",{"message":sub,"name":user_object.name})
        #SRZEEJEC45G4Z2P4KESLBC6U