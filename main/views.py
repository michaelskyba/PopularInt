from django.shortcuts import get_object_or_404, render
from django.http import Http404

from .models import User
import datetime

# GET

# Homepage
def index(request):
    return render(request, 'main/index.html', {})

# Register page
def register(request):
    context = {}
    return render(request, 'main/register.html', context)

# Log in page
def login(request):
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

# POST

# Register POST submission
def register_submit(request):
    # If the user uses the web inspector to try to delete form elements, it will raise an error here
    try:
        if request.POST["password_confirm"] != request.POST["password"]:
            # Make sure passwords match
            context = {"message": "Passwords do not match."}
            return render(request, 'main/register.html', context)

        if not request.POST["password"]:
            # Make sure you have something in the "password" input
            context = {"message": "You need to provide a password."}
            return render(request, 'main/register.html', context)

        if not request.POST["username"]:
            # Make sure a username is provided
            context = {"message": "You need to provide a username."}
            return render(request, 'main/register.html', context)

    except:
        context = {"message": "Nice try!"}
        return render(request, 'main/register.html', context)

    # Make sure user didn't inject any funky characters
    for letter in request.POST["username"]:
        if letter not in "bcdfghjklmnpqrstvwxz":
            context = {"message": "Nice try!"}
            return render(request, 'main/register.html', context)

    # Makre sure user didn't make the username longer/shorter
    if len(request.POST["username"]) != 5:
        context = {"message": "Nice try!"}
        return render(request, 'main/register.html', context)

    # Make sure username doesn't already exist
    try:
        user = User.objects.get(username_text=request.POST["username"])
        context = {"message": "Username taken."}
        return render(request, 'main/register.html', context)

    except User.DoesNotExist:
        # Register user
        new_user = User.objects.create(username_text=request.POST["username"], password_text=request.POST["password"], registration_date=datetime.datetime.now())
        new_user.save()

        context = {"message": "Registered successfully."}
        return render(request, 'main/register.html', context)

# Log in POST submission
def login_submit(request):
    context = {}
    return render(request, 'main/login.html', context)

# Vote POST submission
def vote_submit(request):
    context = {}
    return render(request, 'main/post.html', context)

