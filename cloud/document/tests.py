from django.test import TestCase
from datetime import datetime
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Document
import os.path
from pathlib import Path

class DocumentTestCases(TestCase):

    @classmethod
    def setUpTestData(cls):
        document = SimpleUploadedFile('document222.txt', content=b'', content_type='aplication/document')
        document = Document.objects.create(
            descriptions='Djnago',
            document=document,
            slug='xwfsekjldhgreoym',
            date_upload=datetime(2021, 4, 4, 7, 41, 0, 806429)
        )

    def test_document_value_str_field(self):
        document_db = Document.objects.get(id=1)

        descriptions = document_db.descriptions
        slug = document_db.slug

        self.assertEquals(descriptions, 'Djnago')
        self.assertTrue(len(slug) != 0)

    def test_document_invalid_document(self):
        document_db = Document.objects.get(id=1)
        BASE_DIR = Path(__file__).resolve().parent.parent

        self.assertEquals(str(document_db.document),'media/document/document222.txt')

        os.remove(os.path.join(BASE_DIR,'media\media\document', 'document222.txt'))
        #Если тест прошёл неудачно файл в файловой системе не удалиться, удалять нужно будет в ручную
        #Нужно пофиксить это

