from django.shortcuts import render
from django.views.generic import View
from .models import PointOfInterest
from django.conf import settings
# Create your views here.
class ListView(View):
	def get(self, request):
		places = PointOfInterest.objects.all()
		keymap = settings.GEOPOSITION_GOOGLE_MAPS_API_KEY
		template_name = 'places.html'
		context={
		'places':places, 
		'keymap':keymap
		}
		return render(request, template_name, context)
