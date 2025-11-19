from django.contrib import admin

from .models import Siswa, Kota

@admin.register(Kota)
class KotaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama')
    search_fields = ('nama',)

@admin.register(Siswa)
class SiswaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama', 'nim', 'kota', 'jenis_kelamin', 'tanggal_lahir')
    list_filter = ('jenis_kelamin', 'kota')
    search_fields = ('nama', 'nim')