import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    username_text = models.CharField(max_length=20)
    password_text = models.CharField(max_length=200)
    registration_date = models.DateTimeField()

    def __str__(self):
        return self.username_text

    def was_published_recently(self):
        return self.registration_date >= timezone.now() - datetime.timedelta(days=1)

class Integer(models.Model):
    value_chosen = models.IntegerField()

    def __str__(self):
        return str(self.value_chosen)

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    integer = models.ForeignKey(Integer, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.integer)
