from unicodedata import name
from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('', views.index, name='home'),
    path('airport', views.airport, name='airport'),
    path('flicompany', views.flicompany, name='flicompany'),
    path('flight', views.flight, name='flight'),
    path('ticket', views.ticket, name='ticket'),
    path('store', views.store, name='store'),
    path('worker', views.worker, name='worker'),
    path('supplier', views.supplier, name='supplier'),
    path('bookingagent', views.bookingagent, name='bookingagent'),

]
