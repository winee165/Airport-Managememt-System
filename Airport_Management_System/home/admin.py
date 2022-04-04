from django.contrib import admin
from .models import Airport, FlightCompany, Flight
# Register your models here.

admin.site.register(Airport)
admin.site.register(FlightCompany)
admin.site.register(Flight)
