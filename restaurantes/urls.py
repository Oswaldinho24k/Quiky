from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$', views.RestListView.as_view(), name="lista"), 
	url(r'^(?P<slug>[-\w]+)/$', views.RestDetailView.as_view(), name="detalle"), 
	
]