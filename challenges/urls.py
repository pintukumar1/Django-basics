from operator import index
from django.urls import path
from . import views

urlpatterns = [
    # path("january", views.index),
    # path("february", views.indexForFeb)
    path("", views.index),
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]