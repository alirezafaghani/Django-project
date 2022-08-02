from django.db import models
from django import middleware


class Todo(models.Model):
    objects = None
    title =   models.CharField(max_length = 200)
    body =    models.TextField()
    email =   models.EmailField()

    created = models.DateTimeField()

