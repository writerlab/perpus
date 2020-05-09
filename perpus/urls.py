from django.contrib import admin
from django.urls import path
from perpustakaan.views import buku, penerbit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buku/', buku),
    path('penerbit/', penerbit),
]
