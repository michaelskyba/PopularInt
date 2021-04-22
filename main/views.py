from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Welcome to PopularInt.")

def register(request):
    return HttpResponse("Create a free account.")

def login(request):
    return HttpResponse("Log into your PopularInt account.")

def leaderboard(request):
    return HttpResponse("Here are the top integers:")

def vote(request):
    return HttpResponse("Choose an integer to upvote.")

def view_integer(request):
    return HttpResponse("You're looking at the %s integer." % chosen_integer)

def profile(request):
    return HttpResponse("You're looking at %s's profile." % user_id)

