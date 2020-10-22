from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Lokasi(models.Model):
	nama_lok = models.CharField(max_length=255, null=True)

	def __str__(self):
		return self.nama_lok

class Tipe(models.Model):
	tipe_unit = models.CharField(max_length=5, null=True)

	def __str__(self):
		return self.tipe_unit

class Unit(models.Model):
	STATUS = (
			('Tersedia', 'Tersedia'),
			('Tidak Tersedia', 'Tidak Tersedia'),
			('Dipesan', 'Dipesan'),
			)

	no_unit = models.CharField(max_length = 5, null=True)
	lokasi = models.ForeignKey(Lokasi, null=True, on_delete=models.SET_NULL)
	tipe = models.ForeignKey(Tipe, null=True, on_delete=models.SET_NULL)
	status_rumah = models.CharField(max_length = 200, null=True, choices=STATUS)

	def __str__(self):
		return self.no_unit

class Harga(models.Model):
	harga_unit = models.IntegerField(null=True)
	no_unit = models.ForeignKey(Unit, null=True, on_delete=models.SET_NULL)
	
	def __str__(self):
		return str(self.no_unit) if self.no_unit else ''

class Pelanggan(models.Model):
	user = models.OneToOneField(User, related_name='profile', null=True, on_delete=models.CASCADE)
	nama = models.CharField(max_length = 255, null=True)
	no_telp = models.CharField(max_length = 15, null=True)
	email = models.CharField(max_length = 200, null=True)
	no_unit = models.ForeignKey(Unit, null=True, on_delete=models.SET_NULL)
	
	def __str__(self):
		return self.nama

class Angsuran(models.Model):
	ANGSURAN = (
			('1', '1'),
			('2', '2'),
			('3', '3'),
			('4', '4'),
			('5', '5'),
			)

	nama = models.ForeignKey(Pelanggan, null=True, on_delete=models.SET_NULL)
	uang_muka = models.IntegerField(null=True)
	lama_angsur = models.CharField(max_length=255, null=True, choices=ANGSURAN)

	def __str__(self):
		return str(self.nama) if self.nama else ''

class StatusEnum(object):
    	Lunas = 'Lunas'
    	Belumlunas = 'Belum Lunas'
	
class Administrasi(models.Model):
	STATUS = (
			('Lunas', 'Lunas'),
			('Belum Bayar', 'Belum Bayar'),
			)
	ANGSURAN = (
			('1', '1'),
			('2', '2'),
			('3', '3'),
			('4', '4'),
			('5', '5'),
			)

	tanggal = models.DateTimeField(auto_now_add=True, null=True)
	nama = models.ForeignKey(Pelanggan, null=True, on_delete=models.SET_NULL)
	no_unit = models.ForeignKey(Unit, null=True, on_delete=models.SET_NULL)
	angsuran_ke = models.CharField(max_length=255, null=True, choices=ANGSURAN)
	biaya_angsur = models.IntegerField(null=True)
	status_bayar = models.CharField(max_length=255, null=True, choices=STATUS, default=StatusEnum.Lunas)
	
	def __str__(self):
		return str(self.nama) if self.nama else ''

class Booking(models.Model):
	nama = models.CharField(max_length=255, null=True)
	email = models.CharField(max_length = 200, null=True)
	no_telp = models.CharField(max_length = 15, null=True)
	no_unit = models.ForeignKey(Unit, null=True, on_delete=models.SET_NULL)
	tanggal = models.DateTimeField(auto_now_add=True, null=True)