from models import Bookmark, Tag
from django.contrib import admin

# Register your models here.

class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('url', 'title', 'owner', 'date_updated')
    list_filter = ('title', 'owner__username', 'tags')
    search_fields = ['url', 'title', 'owner__username','tags__name']
    readonly_fields = ('date_created', 'date_updated')

admin.site.register(Bookmark,BookmarkAdmin)
admin.site.register(Tag)