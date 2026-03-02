from django.db import models


class Technology(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Technology'
        verbose_name_plural = 'Technologies'

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    imagem = models.ImageField(upload_to='projects/', null=True, blank=True)
    technologies = models.ManyToManyField(
        Technology,
        related_name='projects',
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title