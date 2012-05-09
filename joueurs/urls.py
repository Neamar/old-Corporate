from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from joueurs.models import Player

urlpatterns = patterns('',
	url(r'^$',
		ListView.as_view(
			queryset=Player.objects.all())),
	url(r'^(?P<slug>[a-z-]+)$', 'joueurs.views.detail'),
)
