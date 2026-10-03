from django.db import models


class IntelligenceSignal(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default='observed')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
