from import_export import resources
from perpustakaan.models import Buku
from import_export.fields import Field

class BukuResource(resources.ModelResource):
  kelompok_id__nama = Field(attribute='kelompok_id', column_name='kelompok')

  class Meta:
    model = Buku
    fields = ['judul', 'tanggal', 'kelompok_id__nama', 'penerbit', 'jumlah']
    export_order = ['judul', 'kelompok_id__nama', 'tanggal', 'penerbit', 'jumlah']