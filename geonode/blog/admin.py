from django.contrib import admin
from .models.post_models import Post

class PostAdmin(admin.ModelAdmin):
    # list_display = ('category', 'title', 'slug', 'author', 'image', 'image_credit', 'body', 'date_published', 'status')
    list_display = ('title', 'slug', 'author', 'body', 'date_published', 'status')
    list_filter = ('status', 'date_created', 'date_published', 'author',)
    search_fields = ('title', 'body',)
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'date_published'
    ordering = ['status', '-date_created',]
    # readonly_fields = ('views',)


# Registers the article model at the admin backend.
# admin.site.register(Post)
admin.site.register(Post, PostAdmin)
