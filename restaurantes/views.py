from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.conf import settings
from .models import Restaurante, Location
# Create your views here.
class RestListView(View):
	def get(self, request):
		#places = Location.objects.all()
		#keymap = settings.GEOPOSITION_GOOGLE_MAPS_API_KEY
		template_name = 'restaurantes/lista.html'
		restaurantes = Restaurante.objects.all()
		
		context={
		#'places':places, 
		#'keymap':keymap
		'restaurantes': restaurantes
		}
		return render(request, template_name, context)

class RestDetailView(View):
	def get(self, request, slug):
		restaurante = get_object_or_404(Restaurante, slug=slug)
		keymap = settings.GEOPOSITION_GOOGLE_MAPS_API_KEY
		template_name = 'restaurantes/detail.html'
		context ={
		'restaurante':restaurante, 
		'keymap': keymap
		}
		return render(request, template_name, context)


