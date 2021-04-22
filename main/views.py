from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import User

# Create your views here.
def index(request):
    return render(request, 'main/index.html', {})

def register(request):
    return HttpResponse("Create a free account.")

def login(request):
    return HttpResponse("Log into your PopularInt account.")

def leaderboard(request):
    return HttpResponse("Here are the top integers:")

def vote(request):
    return HttpResponse("Choose an integer to upvote.")

def view_integer(request, chosen_integer):
    return HttpResponse("You're looking at the %s integer." % chosen_integer)

def profile(request, username):
    # Make sure user exists
    try:
        user = User.objects.get(username_text=username)
    except User.DoesNotExist:
        raise Http404("No user with name '%s'." % username)

    # List of integers
    integers = []
    for vote in user.vote_set.all():
        integers.append(vote)

    # rest of the context
    context = {
            "username": user.username_text,
            "register": user.registration_date,
            "password": user.password_text,
            "integers": integers
            }
    # funny how all of them line up

    return render(request, 'main/profile.html', context)

