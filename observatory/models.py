from django.db import models


class Organisation(models.Model):
    """Phase 9 — Institutional Collaboration. Represents a contributing institution."""

    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Organisation'
        verbose_name_plural = 'Organisations'

    def __str__(self):
        return self.name


class IntelligenceSignal(models.Model):
    """Phase 1 — Observe. The primary unit of observation."""

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
    # Phase 3 — Geospatial
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    # Phase 9 — Institutional attribution
    organisation = models.ForeignKey(
        Organisation, null=True, blank=True,
        on_delete=models.SET_NULL, related_name='signals',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Intelligence Signal'
        verbose_name_plural = 'Intelligence Signals'

    def __str__(self):
        return self.title

    @property
    def has_coordinates(self):
        return self.latitude is not None and self.longitude is not None


class Evidence(models.Model):
    """Phase 2 — Evidence Management. Supports a signal with documented evidence."""

    class EvidenceType(models.TextChoices):
        OBSERVATION = 'Observation', 'Observation'
        REPORT = 'Report', 'Report'
        DATA = 'Data', 'Data'
        TESTIMONY = 'Testimony', 'Testimony'
        MEDIA = 'Media', 'Media'
        OTHER = 'Other', 'Other'

    class Reliability(models.TextChoices):
        UNVERIFIED = 'Unverified', 'Unverified'
        PLAUSIBLE = 'Plausible', 'Plausible'
        CONFIRMED = 'Confirmed', 'Confirmed'

    signal = models.ForeignKey(IntelligenceSignal, on_delete=models.CASCADE, related_name='evidence')
    title = models.CharField(max_length=200)
    evidence_type = models.CharField(max_length=50, choices=EvidenceType.choices, default=EvidenceType.OBSERVATION)
    reliability = models.CharField(max_length=50, choices=Reliability.choices, default=Reliability.UNVERIFIED)
    description = models.TextField(blank=True)
    source_url = models.URLField(blank=True)
    collected_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-collected_at']
        verbose_name = 'Evidence'
        verbose_name_plural = 'Evidence'

    def __str__(self):
        return f'{self.title} ({self.signal.title})'


class Assessment(models.Model):
    """Phase 5 — Decision Support. A structured analysis of a signal."""

    class Priority(models.TextChoices):
        LOW = 'Low', 'Low'
        MEDIUM = 'Medium', 'Medium'
        HIGH = 'High', 'High'
        CRITICAL = 'Critical', 'Critical'

    signal = models.OneToOneField(IntelligenceSignal, on_delete=models.CASCADE, related_name='assessment')
    summary = models.TextField()
    priority = models.CharField(max_length=20, choices=Priority.choices, default=Priority.MEDIUM)
    recommendation = models.TextField(blank=True)
    assessed_by = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Assessment'
        verbose_name_plural = 'Assessments'

    def __str__(self):
        return f'Assessment: {self.signal.title}'


class Opportunity(models.Model):
    """Phase 4 — Opportunity Mapping. An actionable opportunity arising from a signal."""

    class OpportunityStatus(models.TextChoices):
        IDENTIFIED = 'Identified', 'Identified'
        SCOPING = 'Scoping', 'Scoping'
        READY = 'Ready', 'Ready'
        ACTIVE = 'Active', 'Active'
        CLOSED = 'Closed', 'Closed'

    signal = models.ForeignKey(IntelligenceSignal, on_delete=models.CASCADE, related_name='opportunities')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=50, choices=OpportunityStatus.choices, default=OpportunityStatus.IDENTIFIED)
    location = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Opportunity'
        verbose_name_plural = 'Opportunities'

    def __str__(self):
        return self.title


class ActionItem(models.Model):
    """Phase 7 — Human-AI Coordination. A concrete action assigned to coordinate a response."""

    class ActionStatus(models.TextChoices):
        PROPOSED = 'Proposed', 'Proposed'
        ASSIGNED = 'Assigned', 'Assigned'
        IN_PROGRESS = 'In Progress', 'In Progress'
        COMPLETE = 'Complete', 'Complete'
        CANCELLED = 'Cancelled', 'Cancelled'

    opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE, related_name='actions')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    assigned_to = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=50, choices=ActionStatus.choices, default=ActionStatus.PROPOSED)
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['due_date', '-created_at']
        verbose_name = 'Action Item'
        verbose_name_plural = 'Action Items'

    def __str__(self):
        return self.title


class ImpactRecord(models.Model):
    """Phase 8 — Impact Measurement. Records a measurable outcome from an action."""

    class ImpactType(models.TextChoices):
        ENVIRONMENTAL = 'Environmental', 'Environmental'
        SOCIAL = 'Social', 'Social'
        ECONOMIC = 'Economic', 'Economic'
        INSTITUTIONAL = 'Institutional', 'Institutional'

    action = models.ForeignKey(ActionItem, on_delete=models.CASCADE, related_name='impacts')
    title = models.CharField(max_length=200)
    impact_type = models.CharField(max_length=50, choices=ImpactType.choices)
    description = models.TextField(blank=True)
    metric = models.CharField(max_length=200, blank=True, help_text='e.g. "500 households reached"')
    recorded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-recorded_at']
        verbose_name = 'Impact Record'
        verbose_name_plural = 'Impact Records'

    def __str__(self):
        return f'{self.title} ({self.action.title})'
