from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from .models import Airport, FlightCompany
from .forms import AirportForm, FliCompanyForm, FlightForm, TicketForm, StoreForm, WorkerForm, SupplierForm, BookingAgentForm
from .forms import NewUserForm
from django.contrib.auth import login, authenticate #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this

# Create your views here.
# def index(request):
#     return render(request, "index.html")

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
    return render(request, 'flightc.html')

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

def bookingagent(request):
    if request.method == "POST":
        form = BookingAgentForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = BookingAgentForm()
    return render(request, 'booking-agent.html')

def index(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('id_username')
			password = form.cleaned_data.get('id_password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="index.html", context={"login_form":form})