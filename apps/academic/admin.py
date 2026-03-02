from django.contrib import admin
from .models import AcademicBackground


@admin.register(AcademicBackground)
class AcademicBackgroundAdmin(admin.ModelAdmin):
    list_display = ('course', 'institution', 'start_date', 'end_date')
    search_fields = ('course', 'institution', 'profile__name')
    list_filter = ('start_date', 'end_date', 'institution')
    readonly_fields = ('created_at',)
    ordering = ('-end_date', '-start_date')

    fieldsets = (
        ('Detalhes Acadêmicos', {
            'fields': ('profile', 'course', 'institution')
        }),
        ('Período', {
            'fields': ('start_date', 'end_date')
        }),
        ('Descrição', {
            'fields': ('description',)
        }),
        ('Metadados', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )