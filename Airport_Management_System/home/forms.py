from django import forms
from .models import Airport

class AirportForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = '__all__'