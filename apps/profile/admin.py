<<<<<<< HEAD
from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'email', 'created_at')
    search_fields = ('name', 'email', 'role')
    list_filter = ('created_at', 'role')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'photo', 'role')
        }),
        ('Contact Information', {
            'fields': ('email', 'linkedin', 'github')
        }),
        ('Bio', {
            'fields': ('description',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
=======
from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'email', 'created_at')
    search_fields = ('name', 'email', 'role')
    list_filter = ('created_at', 'role')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'photo', 'role')
        }),
        ('Contact Information', {
            'fields': ('email', 'linkedin', 'github')
        }),
        ('Bio', {
            'fields': ('description',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
>>>>>>> origin/main
