from django.shortcuts import get_object_or_404, render
from django.http import Http404

from .models import User

# Create your views here.
# Homepage
def index(request):
    return render(request, 'main/index.html', {})

# Register page
def register(request):
    context = {}
    return render(request, 'main/register.html', context)

# Register POST submission
def register_submit(request):
    context = {"message": "Successfully registered."}

    try:
        if request.POST["password_confirm"] != request.POST["password"]:
            context = {"message": "Passwords do not match."}

        if not request.POST["password"]:
            context = {"message": "You need to provide a password."}

        if not request.POST["username"]:
            context = {"message": "You need to provide a username."}
    except:
        context = {"message": "tf are you doing?"}

    return render(request, 'main/register.html', context)

# Log in page
def login(request):
    context = {}
    return render(request, 'main/login.html', context)

def login_submit(request):
    context = {}
    return render(request, 'main/login.html', context)

# Leaderboard page
def leaderboard(request):
    context = {}
    return render(request, 'main/leaderboard.html', context)

# Vote page
def vote(request):
    context = {}
    return render(request, 'main/vote.html', context)

# View an integer
def view_integer(request, chosen_integer):
    context = {
            "chosen_integer": chosen_integer
            }
    return render(request, 'main/view_integer.html', context)

# Profile page
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

