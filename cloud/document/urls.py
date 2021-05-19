from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import *

urlpatterns = [
    path('', views.index, name='indexView'),
    path('upload/', DocumentUpload, name='document_upload'),
    path('documentAll/', DocumentAll, name='documentAll'),
    path('documentAll/<slug:slug>', DocumentDownload, name='documentDownload'),
    path('documentAll/<slug:slug>/detail', DocumentDetailView.as_view(), name='document_detail'),
    path('documentAll/<slug:slug>/delete', DocumentDeleteView.as_view(), name='document_delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()