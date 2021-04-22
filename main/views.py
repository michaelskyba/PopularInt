from django.shortcuts import get_object_or_404, render
from django.http import Http404

from .models import User

# Create your views here.
def index(request):
    return render(request, 'main/index.html', {})

def register(request):
    context = {
            "chosen_integer": chosen_integer
            }
    return render(request, 'main/register.html', context)

def login(request):
    context = {
            "chosen_integer": chosen_integer
            }
    return render(request, 'main/login.html', context)

def leaderboard(request):
    context = {
            "chosen_integer": chosen_integer
            }
    return render(request, 'main/leaderboard.html', context)

def vote(request):
    context = {
            "chosen_integer": chosen_integer
            }
    return render(request, 'main/vote.html', context)

def view_integer(request, chosen_integer):
    context = {
            "chosen_integer": chosen_integer
            }
    return render(request, 'main/view_integer.html', context)

def profile(request, username):
    # Make sure user exists
    user = get_object_or_404(User, username_text=username)

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

    return render(request, 'main/profile.html', context)

