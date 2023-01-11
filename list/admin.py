from django.contrib import admin
from .models import Media, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Media)
class MediaAdmin(SummernoteModelAdmin):

    list_display = ('title', 'platform', 'genre', 'type', 'status')
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'platform', 'genre', 'type')
    summernote_fields = ('description')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)