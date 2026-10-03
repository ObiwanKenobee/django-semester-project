from django.contrib import admin
from .models import IntelligenceSignal


@admin.register(IntelligenceSignal)
class IntelligenceSignalAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'location', 'created_at')
    list_filter = ('category', 'status')
    search_fields = ('title', 'description', 'location')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
