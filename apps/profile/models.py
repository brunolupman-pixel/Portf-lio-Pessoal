from django.db import models
from django.core.validators import URLValidator


class Profile(models.Model):
    """
    User profile model for portfolio main information.
    Stores personal details, photo, and social links.
    """
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='profile/', null=True, blank=True)
    role = models.CharField(max_length=100, help_text="e.g., Full-Stack Engineer, Student")
    description = models.TextField(help_text="Professional summary or bio")
    email = models.EmailField(unique=True)
    linkedin = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f"{self.name} - {self.role}"