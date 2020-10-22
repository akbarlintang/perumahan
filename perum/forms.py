from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *
from django.views.generic import CreateView
from django import forms

class PelangganForm(forms.ModelForm):
	class Meta:
		model = Pelanggan
		fields = '__all__'
		exclude = ['user']

class UnitForm(ModelForm):
	class Meta:
		model = Unit
		fields = '__all__'

class AdministrasiForm(ModelForm):
	class Meta:
		model = Administrasi
		fields = '__all__'

class BookingForm(ModelForm):
	class Meta:
		model = Booking
		fields = '__all__'
	
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']