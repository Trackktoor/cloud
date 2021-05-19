from django.contrib import admin
from .models import News

class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"title": ("title",)}

admin.site.register(News, NewsAdmin)