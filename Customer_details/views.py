from django.shortcuts import render
from Customer_details.models import input
from django.conf import settings
from django.core.mail import send_mail
from django.utils.datastructures import MultiValueDictKeyError
from django import forms

# Create your views here.


def FETCH(request):
    if request.method == "POST":
        name = request.POST['name']
        try:
            age = int(request.POST['age'])
        except:
            raise ValueError

        city = request.POST['city']
        state = request.POST['state']

        try:
            check = request.POST['check']
        except:
            raise ValueError

        # message = (request.POST['age']) + request.POST['city'] + request.POST['state']

    ins = input(name=name, age=age, city=city, state=state, check=check)
    ins.save()
    # subject = 'welcome to GFG world'
    # #message = 'Hi thank you for registering in geeksforgeeks.'
    # email_from = settings.EMAIL_HOST_USER
    # recipient_list = ['raghulbaskar1123@gmail.com', ]
    # send_mail(subject, message, email_from, recipient_list)

    return render(request, 'details.html')


def SHOW(request):
    posts = input.objects.all()
    c = dict({'posts': posts})
    return render(request, 'output.html', c)
