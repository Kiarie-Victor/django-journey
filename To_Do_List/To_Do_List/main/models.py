from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ToDoList(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Items(models.Model):
    author = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text} - {self.description}"
