from django.contrib import admin
from .models import Airport, FlightCompany, Flight, Ticket, Store
# Register your models here.

admin.site.register(Airport)
admin.site.register(FlightCompany)
admin.site.register(Flight)
admin.site.register(Ticket)
admin.site.register(Store)

