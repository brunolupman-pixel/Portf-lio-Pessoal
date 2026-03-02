from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'email', 'created_at', 'is_read')
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('created_at', 'is_read')
    readonly_fields = ('created_at',)
    
    fieldsets = (
        ('Informações da Mensagem', {
            'fields': ('subject', 'is_read')
        }),
        ('Remetente', {
            'fields': ('name', 'email')
        }),
        ('Mensagem', {
            'fields': ('message',)
        }),
        ('Metadados', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    def has_add_permission(self, request):
        return False