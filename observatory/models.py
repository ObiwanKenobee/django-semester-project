from django.db import models


class IntelligenceSignal(models.Model):

    class Category(models.TextChoices):
        WATER = 'Water', 'Water'
        INFRASTRUCTURE = 'Infrastructure', 'Infrastructure'
        ECOLOGY = 'Ecology', 'Ecology'
        FOOD = 'Food', 'Food'
        ENERGY = 'Energy', 'Energy'
        CLIMATE = 'Climate', 'Climate'
        COMMUNITY = 'Community', 'Community'
        HEALTH = 'Health', 'Health'

    class Status(models.TextChoices):
        OBSERVED = 'Observed', 'Observed'
        REVIEWING = 'Reviewing', 'Reviewing'
        VERIFIED = 'Verified', 'Verified'
        ACTIONABLE = 'Actionable', 'Actionable'
        RESOLVED = 'Resolved', 'Resolved'

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100, choices=Category.choices)
    status = models.CharField(max_length=50, choices=Status.choices, default=Status.OBSERVED)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=200, blank=True)
    source = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Intelligence Signal'
        verbose_name_plural = 'Intelligence Signals'

    def __str__(self):
        return self.title
