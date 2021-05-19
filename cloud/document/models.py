from django.db import models
from django.urls import reverse
import os
import random
import string

class Document(models.Model):
    descriptions = models.CharField(max_length=250)
    document = models.FileField(upload_to='media/document')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL" )
    date_upload = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        all_slug = [document.slug for document in Document.objects.all()]
        print(all_slug)
        if not self.id:
            letters = string.ascii_lowercase
            self.slug = ''.join(random.choice(letters) for i in range(16))
            while self.slug in all_slug:
                self.slug = ''.join(random.choice(letters) for i in range(16))
        super(Document, self).save(*args, **kwargs)

    def __str__(self):
        return  self.descriptions