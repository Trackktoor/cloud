from django.contrib import admin
from .models import Document

class DocumentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("descriptions",)}

admin.site.register(Document, DocumentAdmin)



