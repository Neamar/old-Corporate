from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from django.views.generic.simple import direct_to_template
from corporate.models import AbleEntity
from agents.models import Fixer, Yakuza, Agency

urlpatterns = patterns('',
	url(r'^$', 'agents.views.index'),

	#fixers
	url(r'^fixers/$',
		ListView.as_view(
			queryset=Fixer.objects.all())),

	#yakuzas
	url(r'^yakuzas/$',
		ListView.as_view(
			queryset=Yakuza.objects.all())),

	#agences
	url(r'^agences/$',
		ListView.as_view(
			queryset=Agency.objects.all())),
)
