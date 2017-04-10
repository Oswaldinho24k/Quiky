from django.db import models
from django.core.urlresolvers import reverse

from geoposition.fields import GeopositionField
from taggit.managers import TaggableManager

class Location(models.Model):
    name = models.CharField(max_length=100)
    position = GeopositionField()

    def __str__(self):
    	return self.name

class Restaurante(models.Model):
	name = models.CharField(max_length=100)
	desc = models.TextField()
	logo = models.ImageField(upload_to="restaurantes/logos")
	image = models.ImageField(upload_to="restaurantes/images")
	slug = models.SlugField()
	abre = models.TimeField(auto_now_add=False, db_index=True)
	cierra = models.TimeField(auto_now_add=False, db_index=True)

	tags = TaggableManager()
	
	location = models.OneToOneField(Location)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('posts:detalle', args=[self.slug])







