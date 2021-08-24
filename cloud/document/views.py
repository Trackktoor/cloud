from django.conf import settings
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView, DeleteView
from .forms import DocumentForm
from .models import Document
import os

def index(request):
    return render(request, 'main/index.html')

class DocumentDetailView(DetailView):
    model = Document
    template_name = 'main/document_detail.html'
    slug_field = 'slug'
    context_object_name = 'document'

class DocumentDeleteView(DeleteView):
    model = Document
    context_object_name = 'document'
    template_name = 'main/document_delete.html'
    success_url = reverse_lazy('documentAll')

def DocumentUpload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            print(form)
            form.save()
            return redirect('indexView')
    else:
        form = DocumentForm()
    return render(request, 'main/upload_view.html', {
        'form': form
    })

def DocumentAll(request):
    download_list = Document.objects.all()
    return render(request, 'main/document_all_views.html', {'download_list': download_list})

def DocumentDownload(request, path):

    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response = HttpResponse(fh.read(), content_type='aplication/document')
            response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response