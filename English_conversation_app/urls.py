from django.contrib import admin
from django.urls import path, include #추가된 내용

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('chat.urls')), #추가된 내용
]