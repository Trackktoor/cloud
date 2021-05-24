from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('document.urls'), name="home"),
    path('news/', include('news.urls'), name="news"),
    path('admin/', admin.site.urls),
    path('convert/', include('converted_valute.urls'), name='convert')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
