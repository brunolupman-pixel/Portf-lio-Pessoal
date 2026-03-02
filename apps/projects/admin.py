from django.contrib import admin
from .models import Technology, Project


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'get_technologies')
    search_fields = ('title', 'description', 'technologies__name')
    list_filter = ('created_at', 'technologies')
    readonly_fields = ('created_at', 'updated_at')
    filter_horizontal = ('technologies',)

    fieldsets = (
        ('Project Information', {
            'fields': ('title', 'image')
        }),
        ('Description', {
            'fields': ('description',)
        }),
        ('Technologies', {
            'fields': ('technologies',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def get_technologies(self, obj):
        return ', '.join([tech.name for tech in obj.technologies.all()])
    get_technologies.short_description = 'Technologies'
