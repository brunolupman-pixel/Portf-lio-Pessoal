from django.contrib import admin
from .models import AcademicBackground


@admin.register(AcademicBackground)
class AcademicBackgroundAdmin(admin.ModelAdmin):
    list_display = ('course', 'institution', 'start_date', 'end_date', 'profile')
    search_fields = ('course', 'institution', 'profile__name')
    list_filter = ('start_date', 'end_date', 'institution')
    readonly_fields = ('created_at',)
    
    fieldsets = (
        ('Academic Details', {
            'fields': ('profile', 'course', 'institution')
        }),
        ('Duration', {
            'fields': ('start_date', 'end_date')
        }),
        ('Description', {
            'fields': ('description',)
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
