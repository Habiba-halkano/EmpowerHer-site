from django.contrib import admin
from .models import Resources, SupportGroups, BlogPost, Events, Reports
from django.shortcuts import render

# Register your models here.
@admin.register(Resources)
class ResourcesAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'resource_type', 'created_at')
    list_filter = ('title', 'resource_type')
    search_fields = ('title', 'resource_type')
    ordering = ('title',)

@admin.register(SupportGroups)
class SupportGroupsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'contact_info', 'location', 'services')
    list_filter = ('name', 'location')
    search_fields = ('name', 'location')
    ordering = ('name',)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'author', 'published_at')
    list_filter = ('title', 'author')
    search_fields = ('title', 'author')
    ordering = ('title',)

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'location', 'date')
    list_filter = ('title', 'location')
    search_fields = ('title', 'location')
    ordering = ('title',)