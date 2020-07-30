from django.db import models
from django.utils import timezone


class Moo(models.Model):
    text = models.CharField(max_length=150)
    cow = models.CharField(max_length=30)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
