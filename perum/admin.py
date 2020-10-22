from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Pelanggan)
admin.site.register(Unit)
admin.site.register(Administrasi)
admin.site.register(Harga)
admin.site.register(Angsuran)
admin.site.register(Booking)
admin.site.register(Lokasi)
admin.site.register(Tipe)