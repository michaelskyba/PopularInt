from django.db import models

# Create your models here.
class User(models.Model):
    username_text = models.CharField(max_length=20)
    password_text = models.CharField(max_length=200)
    registration_date = models.DateTimeField()

class Integer(models.Model):
    value_chosen = models.IntegerField()

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    integer = models.ForeignKey(Integer, on_delete=models.CASCADE)
