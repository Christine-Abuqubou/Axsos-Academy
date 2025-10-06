from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)  # Email field
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)  # Set automatically when created
    updated_at = models.DateTimeField(auto_now=True)      # Updated automatically on save

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
