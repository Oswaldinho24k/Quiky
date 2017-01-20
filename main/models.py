from django.db import models

# Create your models here.

class Slides(models.Model):
	nombre = models.CharField(max_length=100)
	slide = models.ImageField(upload_to="slides")

	def __str__(self):
		return self.nombre