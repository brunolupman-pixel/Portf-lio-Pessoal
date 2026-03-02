from django.contrib import admin
from django.utils.html import format_html
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'email', 'created_at', 'bio_preview', 'photo_preview')
    search_fields = ('name', 'email', 'role')
    list_filter = ('created_at', 'role')
    readonly_fields = ('created_at', 'updated_at', 'photo_preview')

    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('name', 'photo', 'photo_preview', 'role')
        }),
        ('Informações de Contato', {
            'fields': ('email', 'linkedin', 'github')
        }),
        ('Biografia', {
            'fields': ('description',)
        }),
        ('Registro', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def bio_preview(self, obj):
        return (obj.description[:60] + '...') if obj.description and len(obj.description) > 60 else obj.description
    bio_preview.short_description = 'Bio'

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="width: 45px; height:45px; object-fit:cover;" />', obj.photo.url)
        return '-'
    photo_preview.short_description = 'Foto'
