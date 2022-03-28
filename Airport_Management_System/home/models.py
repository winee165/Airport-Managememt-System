from django.db import models

# Create your models here.
class Airport(models.Model):
    air_id = models.IntegerField(primary_key=True, default=100)
    airport_name = models.CharField(max_length=50, null=False)
    city = models.CharField(max_length=50, null=False)

    def __str__(self):
        return str(self.airport_name + "_" + str(self.air_id))