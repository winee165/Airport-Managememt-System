from django.contrib import admin
from .models import Airport, FlightCompany, Flight, Ticket, Store, Worker, Supplier, BookingAgent
# Register your models here.

admin.site.register(Airport)
admin.site.register(FlightCompany)
admin.site.register(Flight)
admin.site.register(Ticket)
admin.site.register(Store)
admin.site.register(Worker)
admin.site.register(Supplier)
admin.site.register(BookingAgent)

