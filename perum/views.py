from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Sum
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from django.contrib import messages

from .models import *
from .forms import *
from .filters import *
from .decorators import *
import datetime

# Create your views here.
@unauthenticated_user
def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username atau Password salah!')

	context = {}
	return render(request, 'perum/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@unauthenticated_user
def registerPage(request):
	form = CreateUserForm()
	
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='customer')
			user.groups.add(group)
			Pelanggan.objects.create(
				user=user,
				)

			messages.success(request, 'Akun berhasil dibuat untuk ' + username)

			return redirect('login')

	context = {'form':form}
	return render(request, 'perum/register.html', context)

@login_required(login_url='login')
@admin_only
def home(request):
	pelanggans = Pelanggan.objects.all()
	administrasis = Administrasi.objects.all()

	today = datetime.date.today()

	bulan = Administrasi.objects.filter(tanggal__year=today.year, tanggal__month=today.month).aggregate(Sum('biaya_angsur'))['biaya_angsur__sum']
	tahun = Administrasi.objects.filter(tanggal__year=today.year).aggregate(Sum('biaya_angsur'))['biaya_angsur__sum']

	context = {'pelanggans':pelanggans, 'bulan':bulan, 'tahun':tahun, 'administrasis':administrasis}
	return render(request, 'perum/dashboard.html', context)

@login_required(login_url='login')
def unit(request):
	units = Unit.objects.all().order_by('no_unit')

	unitFilter = UnitFilter(request.GET, queryset=units)
	units = unitFilter.qs

	context = {'units':units, 'unitFilter':unitFilter}
	return render(request, 'perum/unit.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def pelanggan(request):
	pelanggans = Pelanggan.objects.all()

	pelangganFilter = PelangganFilter(request.GET, queryset=pelanggans)
	pelanggans = pelangganFilter.qs

	context = {'pelanggans':pelanggans, 'pelangganFilter':pelangganFilter}
	return render(request, 'perum/pelanggan.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def administrasi(request):
	administrasis = Administrasi.objects.all()

	administrasiFilter = AdministrasiFilter(request.GET, queryset=administrasis)
	administrasis = administrasiFilter.qs

	context = {'administrasis':administrasis, 'administrasiFilter':administrasiFilter}
	return render(request, 'perum/administrasi.html', context)
	
def pemesanan(request):
	pemesanan = Booking.objects.all().order_by('tanggal')

	context = {'pemesanan':pemesanan}
	return render(request, 'perum/pemesanan.html', context)

def akun(request, pk):
	akun = Pelanggan.objects.get(id=pk)
	pelanggans = Pelanggan.objects.filter(id=pk)
	adm = Administrasi.objects.filter(nama_id=pk)

	context = {'pelanggans':pelanggans, 'akun':akun, 'adm':adm}
	return render(request, 'perum/akun.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def profil(request):
	nama = request.user.profile.nama
	no_telp = request.user.profile.no_telp
	email = request.user.profile.email
	no_unit = request.user.profile.no_unit

	context = {'nama':nama, 'no_telp':no_telp, 'email':email, 'no_unit':no_unit}
	return render(request, 'perum/profil.html', context)

@login_required(login_url='login')
def angsuran(request, pk):
	adm = Administrasi.objects.filter(nama_id=pk)

	context = {'adm':adm}
	return render(request, 'perum/angsuran.html', context)

def infoUnit(request, pk):
	unit = Unit.objects.filter(id=pk)

	context = {'unit':unit}
	return render(request, 'perum/info_unit.html', context)

def createBooking(request, pk):
	unit = Booking.objects.filter(id=pk)
	form = BookingForm()
	if request.method == 'POST':
		form = BookingForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/unit')

	context = {'form':form, 'unit':unit}
	return render(request, 'perum/form_booking.html', context)

def createPelanggan(request):
	form = PelangganForm()
	if request.method == 'POST':
		form = PelangganForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')

	context = {'form':form}
	return render(request, 'perum/form_pelanggan.html', context)

def ubahPelanggan(request, pk):
	pelanggan = Pelanggan.objects.get(id=pk)
	form = PelangganForm(instance=pelanggan)

	if request.method == 'POST':
		form = PelangganForm(request.POST, instance=pelanggan)
		if form.is_valid():
			form.save()
			return redirect('home')

	context = {'form':form}
	return render(request, 'perum/form_pelanggan.html', context)

def hapusPelanggan(request, pk):
	pelanggan = Pelanggan.objects.get(id=pk)

	if request.method == "POST":
		pelanggan.delete()
		return redirect('pelanggan')

	context = {'pelanggan':pelanggan}
	return render(request, 'perum/hapus_pelanggan.html', context)
	
def createUnit(request):
	form = UnitForm()
	if request.method == 'POST':
		form = UnitForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/unit')

	context = {'form':form}
	return render(request, 'perum/form_unit.html', context)

def ubahUnit(request, pk):
	unit = Unit.objects.get(id=pk)
	form = UnitForm(instance=unit)

	if request.method == 'POST':
		form = UnitForm(request.POST, instance=unit)
		if form.is_valid():
			form.save()
			return redirect('/unit')

	context = {'form':form}
	return render(request, 'perum/form_unit.html', context)

def hapusUnit(request, pk):
	unit = Unit.objects.get(id=pk)

	if request.method == "POST":
		unit.delete()
		return redirect('/unit')

	context = {'unit':unit}
	return render(request, 'perum/hapus_unit.html', context)

def hapusPemesanan(request, pk):
	pemesanan = Booking.objects.get(id=pk)

	if request.method == "POST":
		pemesanan.delete()
		return redirect('/pemesanan')

	context = {'pemesanan':pemesanan}
	return render(request, 'perum/hapus_pemesanan.html', context)


def createAdministrasi(request):
	form = AdministrasiForm()
	if request.method == 'POST':
		form = AdministrasiForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/administrasi')

	context = {'form':form}
	return render(request, 'perum/form_administrasi.html', context)

def pembayaran(request, pk):
	administrasis = Administrasi.objects.filter(id=pk)

	context = {'administrasis':administrasis}
	return render(request, 'perum/pembayaran.html', context)

def pemasukan(request):
	today = datetime.datetime.today()

	bulan = Administrasi.objects.filter(tanggal__year=today.year).filter(tanggal__month=today.month).aggregate(Sum('biaya_angsur'))
	tahun = Administrasi.objects.filter(tanggal__year=today.year).aggregate(Sum('biaya_angsur'))
	hari = Administrasi.objects.filter(tanggal__year=today, tanggal__month=today, tanggal__date=today).aggregate(Sum('biaya_angsur'))
