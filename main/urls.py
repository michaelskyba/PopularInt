from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('leaderboard', views.leaderboard, name='leaderboard'),
    path('vote', views.vote, name='vote'),
    path('view_integer/<int:chosen_integer>', views.view_integer, name='view_integer'),
    path('profile/<str:username>', views.profile, name='profile'),
]
