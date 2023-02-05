from django.contrib import admin
from .models import Post, Comment, Discussion, CommentDisc
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
# From Blog project code insititute


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on',)
    list_filter = ['created_on']
    search_fields = ('name', 'email', 'body')

@admin.register(Discussion)
class DiscussionAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_created')

@admin.register(CommentDisc)
class CommentDiscAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'discussion', 'date_created')