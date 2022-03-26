from django import forms
from .models import *

class UserForm(forms.ModelForm):
	class Meta:
		model = Users
		fields= '__all__'

class ReservationForm(forms.ModelForm):
	class Meta:
		model = Reservation
		fields= '__all__'

class MeetingForm(forms.ModelForm):
	class Meta:
		model = MeetingRooms
		fields= '__all__'
