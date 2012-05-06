from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from corpos.models import Corporation

urlpatterns = patterns('',
	url(r'^$',
		ListView.as_view(
			queryset=Corporation.objects.all())),
	url(r'^(?P<slug>[a-z-]+)$',
		DetailView.as_view(
			model=Corporation)),
)
