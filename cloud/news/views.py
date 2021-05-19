from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm
from django.views.generic import DetailView, DeleteView
from datetime import datetime, timezone

def news_home(request):
    news = News.objects.order_by('-date')[:5]
    date_now = datetime.now()
    return render(request, 'news/news_home.html', {'news': news, 'date_now':date_now})

class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'article'

def NewsUpdateView(request, slug):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news_home')
    else:
        form = NewsForm()
    return render(request, 'news/news_update.html', {
        'form': form
    })

class NewsDeleteView(DeleteView):
    model = News
    template_name = 'news/news_delete.html'
    success_url = '/news'


def newsCreate(request):
    error = ''
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid() and datetime.strptime(request.POST['date'], '%Y-%m-%d').date() >= datetime.now().date():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была не верна или дата была меньше настоящего времени'

    form = NewsForm()

    data = {
        'form':form,
        'error':error
    }

    return render(request, 'news/news_create.html', data)