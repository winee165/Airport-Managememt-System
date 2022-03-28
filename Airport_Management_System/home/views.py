from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from .models import Airport, FlightCompany
from .forms import AirportForm, FliCompanyForm

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

def flicompany(request):
    if request.method == "POST":
        form = FliCompanyForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = FliCompanyForm()
    return render(request, 'FliCompany.html')
