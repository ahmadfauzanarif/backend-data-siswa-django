from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Siswa, Kota
from .serializers import SiswaSerializer, KotaSerializer

class KotaViewSet(viewsets.ModelViewSet):
    queryset = Kota.objects.all()
    serializer_class = KotaSerializer
    permission_classes = [IsAuthenticated]

class SiswaViewSet(viewsets.ModelViewSet):
    queryset = Siswa.objects.select_related('kota').all()
    serializer_class = SiswaSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
