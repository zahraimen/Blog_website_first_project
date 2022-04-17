from django.contrib import admin
from .models import Post


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'datetime_modified',)
    ordering = ('datetime_modified',)


admin.site.register(Post, PostAdmin)
