from django.db import models

from geoposition.fields import GeopositionField

class PointOfInterest(models.Model):
    name = models.CharField(max_length=100)
    position = GeopositionField()

    def __str__(self):
    	return self.name
