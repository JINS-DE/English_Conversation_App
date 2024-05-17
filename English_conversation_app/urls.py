from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import index_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),  # 홈페이지로 설정
    path('',include('chat.urls')),
    path('',include('users.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)