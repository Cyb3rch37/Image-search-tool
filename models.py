## models.py (Logging & Reporting)
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class SearchReport(models.Model):
    image_name = models.CharField(max_length=255)
    match_found = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.image_name} - {'Match' if self.match_found else 'No Match'}"


