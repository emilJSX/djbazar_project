from django.contrib import admin

# Register your models here.
from .models import CommentPost

class CommentInline(admin.TabularInline):
    model = CommentPost


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user','date']
    list_display_links=['user','date']

admin.site.register(CommentPost,CommentAdmin)