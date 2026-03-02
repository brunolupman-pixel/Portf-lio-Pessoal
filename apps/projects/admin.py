from django.contrib import admin
from django.utils.html import format_html
from .models import Technology, Project


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'image_preview', 'get_technologies')
    search_fields = ('title', 'description', 'technologies__name')
    list_filter = ('created_at', 'technologies')
    readonly_fields = ('created_at', 'updated_at', 'image_preview')
    filter_horizontal = ('technologies',)
    ordering = ('-created_at',)

    fieldsets = (
        ('Informações do Projeto', {
            'fields': ('title', 'image', 'image_preview')
        }),
        ('Descrição', {
            'fields': ('description',)
        }),
        ('Tecnologias', {
            'fields': ('technologies',)
        }),
        ('Registro', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def get_technologies(self, obj):
        return ', '.join([tech.name for tech in obj.technologies.all()])
    get_technologies.short_description = 'Technologies'

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 60px; height:60px; object-fit:cover;" />', obj.image.url)
        return '-'
    image_preview.short_description = 'Imagem'