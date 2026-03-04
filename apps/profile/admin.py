from django.contrib import admin
from django.utils.html import format_html
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'email', 'created_at', 'bio_preview', 'foto_preview')
    search_fields = ('name', 'email', 'role')
    list_filter = ('created_at', 'role')
    readonly_fields = ('created_at', 'updated_at', 'foto_preview')

    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('name', 'foto', 'foto_preview', 'role')
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

    def has_add_permission(self, request):
        # allow adding only if no Profile exists
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        # prevent deleting the only profile
        return False

    def bio_preview(self, obj):
        return (obj.description[:60] + '...') if obj.description and len(obj.description) > 60 else obj.description
    bio_preview.short_description = 'Bio'

    def foto_preview(self, obj):
        if obj.foto:
            return format_html('<img src="{}" style="width: 45px; height:45px; object-fit:cover;" />', obj.foto.url)
        return '-'
    foto_preview.short_description = 'Foto'
