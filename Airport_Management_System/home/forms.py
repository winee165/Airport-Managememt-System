from attr import field, fields
from django import forms
from matplotlib.pyplot import cla
from .models import Airport, FlightCompany, Flight, Ticket

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