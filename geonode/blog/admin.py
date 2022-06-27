from django.contrib import admin
from .models.post_models import Post
from .models.category_models import Category

class PostAdmin(admin.ModelAdmin):
    # list_display = ('category', 'title', 'slug', 'author', 'image', 'image_credit', 'body', 'date_published', 'status')
    list_display = ('title', 'category', 'author', 'date_published', 'status')
    list_filter = ('status', 'category', 'date_created', 'date_published', 'author',)
    search_fields = ('title', 'body',)
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'date_published'
    ordering = ['status', '-date_created',]
    # readonly_fields = ('views',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


# Registers the article model at the admin backend.
# admin.site.register(Post)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
