from django.urls import path

from . import views

urlpatterns = [
    # GET
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('leaderboard', views.leaderboard, name='leaderboard'),
    path('vote', views.vote, name='vote'),
    path('view_integer/<int:chosen_integer>', views.view_integer, name='view_integer'),
    path('profile/<str:username>', views.profile, name='profile'),

    # POST
    path('login_submit', views.login_submit, name='login_submit'),
    path('register_submit', views.register_submit, name='register_submit'),
    path('vote_submit', views.vote_submit, name='vote_submit'),
]
