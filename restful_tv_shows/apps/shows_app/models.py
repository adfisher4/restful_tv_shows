from django.db import models

class Show(models.Model):
    name = models.CharField(max_length=255)
    network = models.CharField(max_length=50)
    release_date = models.CharField(max_length=50)
    description = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


