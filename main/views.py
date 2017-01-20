from django.shortcuts import render
from django.views.generic import View
from .models import Slides

# Create your views here.

class Home(View):
	def get(self, request):
		template_name='home.html'

		slides = Slides.objects.all()
		q = len(slides)

		context={
		'slides':slides,
		'q':q
		}

		return render(request, template_name, context)