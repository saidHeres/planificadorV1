# notes/models.py
from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + "\n"+ self.description
