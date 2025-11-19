from django.db import models

class Kota(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama

class Siswa(models.Model):
    JENIS_KELAMIN = (
        ('L', 'Laki-laki'),
        ('P', 'Perempuan'),
    )

    # id otomatis dibuat Django (pk)
    nama = models.CharField(max_length=255)
    nim = models.CharField(max_length=50, unique=True)
    tanggal_lahir = models.DateField()
    jenis_kelamin = models.CharField(max_length=1, choices=JENIS_KELAMIN)
    alamat = models.TextField(blank=True)
    kota = models.ForeignKey(Kota, on_delete=models.SET_NULL, null=True, related_name='siswa')

    def __str__(self):
        return f"{self.nama} ({self.nim})"
