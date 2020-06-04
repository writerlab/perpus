from django.shortcuts import render
from perpustakaan.models import Buku
from perpustakaan.forms import FormBuku

def buku(request):
    # filter: tampilkan semua buku Produktif dan batasi sebanyak 4
    books = Buku.objects.filter(kelompok_id__nama='Produktif')[:4]

    konteks = {
        'books': books,
    }
    return render(request, 'buku.html', konteks)

def penerbit(request):
    return render(request, 'penerbit.html')


def tambah_buku(request):
    if request.POST:
        form = FormBuku(request.POST)
        if form.is_valid():
            form.save()
            form = FormBuku()
            pesan = "Data berhasil disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-buku.html', konteks)
    else:
        form = FormBuku()

        konteks = {
            'form': form,
        }

    return render(request, 'tambah-buku.html', konteks)