from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('recievevideo/', include('recievevideo.urls')),
    path('videocharge/', include('videocharge.urls')),
]
