"""quiky URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
"""
App's Urls
"""
from main import urls as mainUrls
from restaurantes import urls as restaurantesUrls
from django.conf import settings
from django.views.static import serve
from restaurantes import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(mainUrls, namespace='main')),
    #url(r'^lugares/$', views.ListView.as_view()),
    url(r'^restaurantes/', include(restaurantesUrls, namespace="restaurantes")), 
    url(
        regex=r'^media/(?P<path>.*)$',
        view=serve,
        kwargs={'document_root':settings.MEDIA_ROOT}),
]
