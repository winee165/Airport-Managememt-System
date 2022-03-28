from django.shortcuts import render
from django.http import HttpResponse
from .models import Airport
from .forms import AirportForm

# Create your views here.
def index(request):
    return render(request, "index.html")

def airport(request):
    if request.method == "POST":
        form = AirportForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = AirportForm()
    return render(request, 'airport.html')
