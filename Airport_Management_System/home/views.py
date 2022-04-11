from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from .models import Airport, FlightCompany
from .forms import AirportForm, FliCompanyForm, FlightForm, TicketForm, StoreForm, WorkerForm, SupplierForm

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

def flight(request):
    if request.method == "POST":
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = FlightForm()
    return render(request, 'Flight.html')

def ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = TicketForm()
    return render(request, 'ticket.html')

def store(request):
    if request.method == "POST":
        form = StoreForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = StoreForm()
    return render(request, 'store.html')

def worker(request):
    if request.method == "POST":
        form = WorkerForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = WorkerForm()
    return render(request, 'worker.html')

def supplier(request):
    if request.method == "POST":
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = SupplierForm()
    return render(request, 'supplier.html')