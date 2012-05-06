from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from django.views.generic.simple import direct_to_template
from agents.models import Fixer, Yakuza, Agency

urlpatterns = patterns('',
	url(r'^$', direct_to_template, {'template': 'agents/agent_list.html'}),

	#fixers
	url(r'^fixers/$',
		ListView.as_view(
			queryset=Fixer.objects.all())),
	url(r'^fixers/(?P<slug>[a-z-]+)$',
		DetailView.as_view(
			model=Fixer)),

	#yakuzas
	url(r'^yakuzas/$',
		ListView.as_view(
			queryset=Yakuza.objects.all())),
	url(r'^yakuzas/(?P<slug>[a-z-]+)$',
		DetailView.as_view(
			model=Yakuza)),

	#agences
	url(r'^agences/$',
		ListView.as_view(
			queryset=Agency.objects.all())),
	url(r'^agences/(?P<slug>[a-z-]+)$',
		DetailView.as_view(
			model=Agency)),
)
