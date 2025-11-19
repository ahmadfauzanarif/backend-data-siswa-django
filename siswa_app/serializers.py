from rest_framework import serializers
from .models import Siswa, Kota

class KotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kota
        fields = ['id', 'nama']

class SiswaSerializer(serializers.ModelSerializer):
    kota = KotaSerializer(read_only=True)
    id_kota = serializers.PrimaryKeyRelatedField(
        queryset=Kota.objects.all(),
        source='kota',
        write_only=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model = Siswa
        fields = ['id', 'nama', 'nim', 'tanggal_lahir', 'jenis_kelamin', 'alamat', 'kota', 'id_kota']
