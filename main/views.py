from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from django.urls import reverse
from django.db.models import Count

from .models import User, Integer
import datetime

# GET

# Homepage
def index(request):
    try:
        context = {'username': request.session['username']}
    except KeyError:
        context = {}

    return render(request, 'main/index.html', context)

# Register page
def register(request):
    # Redirect to homepage if you're logged in
    try:
        username = request.session['username']
    except KeyError:
        return render(request, 'main/register.html', {})
    else:
        return HttpResponseRedirect(reverse('index'))

# Log in page
def login(request):
    # Redirect to homepage if you're logged in
    try:
        username = request.session['username']
    except KeyError:
        return render(request, 'main/login.html', {})
    else:
        return HttpResponseRedirect(reverse('index'))

# Log out page
def logout(request):
    # Redirect to homepage if you're NOT logged in
    try:
        username = request.session['username']
    except KeyError:
        pass
    else:
        del request.session['username']

    return HttpResponseRedirect(reverse('index'))

# Leaderboard page
def leaderboard(request):
    try:
        context = {'username': request.session['username']}
    except KeyError:
        context = {}

    # Sort integers
    context["integers"] = Integer.objects.all().annotate(num_votes=Count('vote')).order_by('-num_votes')

    return render(request, 'main/leaderboard.html', context)

# Vote page
def vote(request):
    try:
        username = request.session['username']
    except KeyError:
        return HttpsResponseRedirect(reverse("index"))

    return render(request, 'main/vote.html', {"username": username})

# View an integer
def view_integer(request, chosen_integer):
    context = {"integer": chosen_integer}

    # Check if user is signed in
    try:
        context["username"] = request.session['username']
    except KeyError:
        pass

    # See if the integer exists
    try:
        db_integer = Integer.objects.get(value_chosen=int(chosen_integer))
    except:
        pass
    else:
        # Get list of users that voted for this integer
        votes = db_integer.vote_set.all()
        context_users = []
        for vote in votes:
            context_users.append(vote.user)
        context["users"] = context_users

        # Get number
        context["votes"] = len(votes)

    return render(request, 'main/view_integer.html', context)

# Profile page
def profile(request, username):
    try:
        context = {'username': request.session['username']}
    except KeyError:
        context = {}

    # Make sure user exists
    user = get_object_or_404(User, username_text=username)

    # List of integers
    integers = []
    for vote in user.vote_set.all():
        integers.append(vote)

    # rest of the context
    context = {
            'username': user.username_text,
            'register': user.registration_date,
            'password': user.password_text,
            'integers': integers
            }

    return render(request, 'main/profile.html', context)

# POST

# Register POST submission
def register_submit(request):

    # If someone decides to go to /register_submit manually
    if not request.POST:
        return HttpResponseRedirect(reverse('index'))

    # If the user uses the web inspector to try to delete form elements, it will raise an error here
    try:
        if request.POST['password_confirm'] != request.POST['password']:
            # Make sure passwords match
            context = {'message': 'Passwords do not match.'}
            return render(request, 'main/register.html', context)

        if not request.POST['password']:
            # Make sure you have something in the 'password' input
            context = {'message': 'You need to provide a password.'}
            return render(request, 'main/register.html', context)

        if not request.POST['username']:
            # Make sure a username is provided
            context = {'message': 'You need to provide a username.'}
            return render(request, 'main/register.html', context)

    except:
        context = {'message': 'Nice try!'}
        return render(request, 'main/register.html', context)

    # Make sure user didn't inject any funky characters
    for letter in request.POST['username']:
        if letter not in 'bcdfghjklmnpqrstvwxz':
            context = {'message': 'Nice try!'}
            return render(request, 'main/register.html', context)

    # Makre sure user didn't make the username longer/shorter
    if len(request.POST['username']) != 5:
        context = {'message': 'Nice try!'}
        return render(request, 'main/register.html', context)

    # Make sure username doesn't already exist
    try:
        user = User.objects.get(username_text=request.POST['username'])
        context = {'message': 'Username taken.'}
        return render(request, 'main/register.html', context)

    except User.DoesNotExist:
        # Register user
        new_user = User.objects.create(username_text=request.POST['username'], password_text=make_password(request.POST['password']), registration_date=datetime.datetime.now())
        new_user.save()

        # Keep track of them being logged in
        request.session['username'] = request.POST['username']

        return render(request, 'main/index.html', {'username': request.POST["username"], "message": "The registration was successful."})

# Log in POST submission
def login_submit(request):
    # If someone decides to go to /login_submit manually
    if not request.POST:
        return HttpResponseRedirect(reverse('index'))

    # If the user uses the web inspector to try to delete form elements, it will raise an error here
    try:
        username = request.POST['username']
        password = request.POST['password']
    except:
        return render(request, 'main/login.html', {'message': 'Nice try!'})

    # Make sure a user exists with <username>
    try:
        user = User.objects.get(username_text=username)
    except:
        return render(request, 'main/login.html', {'message': 'Invalid username and/or password'})

    # Make sure password is valid
    if check_password(password, user.password_text) == False:
        return render(request, 'main/login.html', {'message': 'Invalid username and/or password'})

    request.session['username'] = username
    return render(request, 'main/index.html', {'username': username, "message": "The login was successful."})

# Vote POST submission
def vote_submit(request):
    # If someone decides to go to /vote_submit manually
    if not request.POST:
        return HttpResponseRedirect(reverse('index'))

    # User deletes the integer field
    try:
        vote = request.POST["integer"]
    except:
        return render(request, 'main/vote.html', {"message": "Nice try.", "username": request.session["username"]})

    # Make sure user gives an integer
    try:
        vote = int(vote)
    except:
        return render(request, 'main/vote.html', {"message": "Nice \"integer\".", "username": request.session["username"]})

    # See if there exists an "Integer" for this integer
    # If not, create one
    try:
        integer_object = Integer.objects.get(value_chosen=vote)
    except:
        integer_object = Integer.objects.create(value_chosen=vote)
        integer_object.save()

    user = User.objects.get(username_text=request.session["username"])

    # Make sure user hasn't already voted for this integer
    try:
        existing_vote = Integer.objects.get(value_chosen=vote).vote_set.get(user=user)
        return render(request, 'main/vote.html', {"message": "You've already voted for this integer...", "username": request.session["username"]})
    except:
        # Add the vote
        integer_object.vote_set.create(user=user)

    # Return template
    return render(request, 'main/vote.html', {"message": "success", "username": request.session["username"]})

