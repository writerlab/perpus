from django.contrib import admin
from django.urls import path
from perpustakaan.views import buku, penerbit, tambah_buku

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buku/', buku),
    path('penerbit/', penerbit),
    path('tambah-buku/', tambah_buku),
]
