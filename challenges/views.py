from unittest import mock
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

import challenges

# Create your views here.

# def january(request):
#     return HttpResponse("Eat no meat for the entire month.")

# def february(request):
#     return HttpResponse("Walk for at least 20 minutes every day.")    

# def march(request):
#     return HttpResponse("Learn Django at least 20 minutes every day.")

monthly_challenges = {
    "january" : "Eat no meat for the entire month.",
    "february": "Walk for at least 20 minutes every day.",
    "march": "Learn Django at least 20 minutes every day",
    "april" : "Eat no meat for the entire month.",
    "may": "Walk for at least 20 minutes every day.",
    "june": "Learn Django at least 20 minutes every day",
    "july" : "Eat no meat for the entire month.",
    "august": "Walk for at least 20 minutes every day.",
    "september": "Learn Django at least 20 minutes every day",
    "october" : "Eat no meat for the entire month.",
    "november": "Walk for at least 20 minutes every day.",
    "december": "Learn Django at least 20 minutes every day"
}

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if(month > len(months)):
        return HttpResponseNotFound("Invalid Month")

    redirect_month = months[month - 1] 
    print(redirect_month)
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month) :
    try:
        challengeText = monthly_challenges[month]
        return HttpResponse(challengeText)
    except: 
        return HttpResponseNotFound("This month is not supported.")        

