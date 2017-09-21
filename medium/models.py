from django.db import models

from django.contrib.auth.models import User


class Note(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=250)
    content = models.TextField()

    def __str__(self):
        return self.title
