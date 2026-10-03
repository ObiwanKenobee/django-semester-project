from django.contrib import admin
from .models import (
    IntelligenceSignal, Evidence, Assessment,
    Opportunity, ActionItem, ImpactRecord, Organisation,
)


class EvidenceInline(admin.TabularInline):
    model = Evidence
    extra = 0
    fields = ('title', 'evidence_type', 'reliability', 'source_url')


class AssessmentInline(admin.StackedInline):
    model = Assessment
    extra = 0
    fields = ('summary', 'priority', 'recommendation', 'assessed_by')


class OpportunityInline(admin.TabularInline):
    model = Opportunity
    extra = 0
    fields = ('title', 'status', 'location')


@admin.register(IntelligenceSignal)
class IntelligenceSignalAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'location', 'organisation', 'created_at')
    list_filter = ('category', 'status', 'organisation')
    search_fields = ('title', 'description', 'location')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    inlines = [EvidenceInline, AssessmentInline, OpportunityInline]


@admin.register(Evidence)
class EvidenceAdmin(admin.ModelAdmin):
    list_display = ('title', 'signal', 'evidence_type', 'reliability', 'collected_at')
    list_filter = ('evidence_type', 'reliability')
    search_fields = ('title', 'description', 'signal__title')
    ordering = ('-collected_at',)


@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('signal', 'priority', 'assessed_by', 'created_at')
    list_filter = ('priority',)
    search_fields = ('signal__title', 'summary', 'recommendation')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')


class ActionItemInline(admin.TabularInline):
    model = ActionItem
    extra = 0
    fields = ('title', 'status', 'assigned_to', 'due_date')


@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    list_display = ('title', 'signal', 'status', 'location', 'created_at')
    list_filter = ('status',)
    search_fields = ('title', 'description', 'signal__title')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    inlines = [ActionItemInline]


class ImpactRecordInline(admin.TabularInline):
    model = ImpactRecord
    extra = 0
    fields = ('title', 'impact_type', 'metric')


@admin.register(ActionItem)
class ActionItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'opportunity', 'status', 'assigned_to', 'due_date')
    list_filter = ('status',)
    search_fields = ('title', 'description', 'assigned_to')
    ordering = ('due_date', '-created_at')
    readonly_fields = ('created_at', 'updated_at')
    inlines = [ImpactRecordInline]


@admin.register(ImpactRecord)
class ImpactRecordAdmin(admin.ModelAdmin):
    list_display = ('title', 'action', 'impact_type', 'metric', 'recorded_at')
    list_filter = ('impact_type',)
    search_fields = ('title', 'description', 'metric')
    ordering = ('-recorded_at',)


@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'website', 'created_at')
    search_fields = ('name', 'country')
    ordering = ('name',)
