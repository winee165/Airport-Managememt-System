# from attr import field, fields
from django import forms
# from matplotlib.pyplot import cla
from .models import Airport, FlightCompany, Flight, Ticket, Store, Worker, Supplier, BookingAgent
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AirportForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = '__all__'

class FliCompanyForm(forms.ModelForm):
    class Meta:
        model = FlightCompany
        fields = '__all__'
        
class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = '__all__'

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = '__all__'

class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = '__all__'

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'

class BookingAgentForm(forms.ModelForm):
    class Meta:
        model = BookingAgent
        fields = '__all__'

class NewUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ("username", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user