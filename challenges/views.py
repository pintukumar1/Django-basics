from unittest import mock
from urllib import request, response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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

def index(request) :
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months: 
        capitalized_month = month.capitalize()
        print("capitalized_month",capitalized_month)
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)    

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
        # responseData = f"<h1>{challengeText}</h1>"
        responseData = render_to_string("challenges/challenge.html")
        return HttpResponse(responseData)
    except: 
        return HttpResponseNotFound("<h1>This month is not supported.</h1>")        

