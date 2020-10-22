from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('unit/', views.unit, name="unit"),
    path('pelanggan/', views.pelanggan, name="pelanggan"),
    path('administrasi/', views.administrasi, name="administrasi"),
    path('pemesanan/', views.pemesanan, name="pemesanan"),
    
    path('profil/', views.profil, name="profil"),
    path('angsuran/<str:pk>/', views.angsuran, name="angsuran"),

    path('akun/<str:pk>/', views.akun, name="akun"),
    path('pembayaran/<str:pk>/', views.pembayaran, name="pembayaran"),
    path('info_unit/<str:pk>/', views.infoUnit, name="info_unit"),

    path('create_pelanggan/', views.createPelanggan, name="create_pelanggan"),
    path('ubah_pelanggan/<str:pk>/', views.ubahPelanggan, name="ubah_pelanggan"),
    path('hapus_pelanggan/<str:pk>/', views.hapusPelanggan, name="hapus_pelanggan"),

    path('create_unit/', views.createUnit, name="create_unit"),
    path('ubah_unit/<str:pk>/', views.ubahUnit, name="ubah_unit"),
    path('hapus_unit/<str:pk>/', views.hapusUnit, name="hapus_unit"),

    path('hapus_pemesanan/<str:pk>/', views.hapusPemesanan, name="hapus_pemesanan"),

    path('create_administrasi/', views.createAdministrasi, name="create_administrasi"),

    path('create_booking/<str:pk>/', views.createBooking, name="create_booking"),
]