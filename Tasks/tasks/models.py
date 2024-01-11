from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100, unique=True)
    is_completed = models.BooleanField()



