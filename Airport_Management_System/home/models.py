from django.db import models

# Create your models here.
class Airport(models.Model):
    air_id = models.IntegerField(primary_key=True, default=100)
    airport_name = models.CharField(max_length=50, null=False)
    city = models.CharField(max_length=50, null=False)

    def __str__(self):
        return str(self.airport_name + "_" + str(self.air_id))


class FlightCompany(models.Model):
    fli_id = models.IntegerField(primary_key=True, default=100)
    company_name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.company_name + "_" + str(self.fli_id)

class Flight(models.Model):
    fli_num = models.IntegerField(primary_key=True, default=100)
    dep_air = models.ForeignKey(Airport, on_delete=models.CASCADE, default=100, related_name='dept_airport')
    arriv_air = models.ForeignKey(Airport, on_delete=models.CASCADE, default=101, related_name='arriv_airport')
    dep_hours = models.DateTimeField()

    def __str__(self):
        return str(self.fli_num)

class Ticket(models.Model):
    seat_class = models.CharField(max_length=10, null=False)
    pass_name = models.CharField(max_length=50, null=False)
    fli_num = models.ForeignKey(Flight, on_delete=models.CASCADE, default=1002)
    price = models.IntegerField(null=False)
    fli_company = models.ForeignKey(FlightCompany, on_delete=models.CASCADE, default=200)
    order_number = models.IntegerField(primary_key=True, default=345)

    def __str__(self):
        return str(self.fli_num) + "_" + self.pass_name

class Store(models.Model):
    name = models.CharField(max_length=50, null=False, primary_key=True)
    type = models.CharField(max_length=50, null=False)
    pro_type = models.CharField(max_length=50, null=False)
    air_id = models.ForeignKey(Airport, on_delete=models.CASCADE, default=200)
    place = models.CharField(max_length=50, null=False)

    def __str__(self):
        return str(self.name) + "_" + str(self.place)

class Worker(models.Model):
    id = models.IntegerField(primary_key=True, default=100)
    name = models.CharField(max_length=50, null=False)
    age = models.IntegerField(null=False)
    payment = models.CharField(max_length=50, null=False)
    str_name = models.ForeignKey(Store, on_delete=models.CASCADE)
    job = models.CharField(max_length=50, null=False)
    air_id = models.ForeignKey(Airport, on_delete=models.CASCADE, default=100)

    def __str__(self):
        return self.name + "_" + str(self.id)

class Supplier(models.Model):
    id = models.IntegerField(primary_key=True, default=400)
    type = models.CharField(max_length=50, null=False)

    def __str__(self):
        return str(self.id) + "_" + str(self.type)

class BookingAgent(models.Model):
    id = models.IntegerField(primary_key=True, default=400)
    comp_name = models.CharField(max_length=50, null=False)
    ag_name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return str(self.ag_name) + "_" + str(self.id)

