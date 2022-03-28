from attr import field
from django import forms
from .models import Airport, FlightCompany

class AirportForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = '__all__'

class FliCompanyForm(forms.ModelForm):
    class Meta:
        model = FlightCompany
        fields = '__all__'
        