from django.db import models
from apps.profile.models import Profile


class AcademicBackground(models.Model):
    """
    Academic background model for educational history.
    Linked to user profile with foreign key relationship.
    """
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='academic_background'
    )
    course = models.CharField(max_length=255, help_text="e.g., Bachelor's in Computer Science")
    institution = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True, help_text="Leave blank if currently enrolled")
    description = models.TextField(blank=True, help_text="GPA, achievements, relevant coursework, etc.")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-end_date', '-start_date']
        verbose_name = 'Academic Background'
        verbose_name_plural = 'Academic Backgrounds'

    def __str__(self):
        return f"{self.course} - {self.institution} ({self.start_date.year})"