from django.contrib import admin

from .models import  Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'article', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'body')

admin.site.register(Comment, CommentAdmin)
# Register your models here.
