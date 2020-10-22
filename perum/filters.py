import django_filters
from django_filters import *

from .models import *

class PelangganFilter(django_filters.FilterSet):
	nama = CharFilter(field_name='nama', lookup_expr='icontains', label='Nama')
	no_unit = CharFilter(field_name='no_unit', lookup_expr='icontains', label='No. Unit')

	class Meta:
		model = Pelanggan
		fields = '__all__'
		exclude = ['no_telp', 'email']

class UnitFilter(django_filters.FilterSet):
	tipe = CharFilter(field_name='tipe', lookup_expr='icontains', label='Tipe Unit')

	class Meta:
		model = Unit
		fields = '__all__'
		exclude = ['no_unit']

class AdministrasiFilter(django_filters.FilterSet):
	nama__nama = CharFilter(field_name='nama', lookup_expr='icontains', label='Nama')
	no_unit__no_unit = CharFilter(field_name='no_unit', lookup_expr='icontains', label='No. Unit')

	class Meta:
		model = Administrasi
		fields = '__all__'
		exclude = ['angsuran_ke', 'status_bayar', 'tanggal']