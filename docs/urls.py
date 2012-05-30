from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from docs.models import Rule
from corpos.models import Corporation

urlpatterns = patterns('',
	url(r'^$',
		ListView.as_view(
			queryset=Rule.objects.all())),
	url(r'^effets$',
		ListView.as_view(
			queryset=Corporation.objects.all(),
			 template_name='docs/effets.html')),
	url(r'^(?P<slug>[a-z-]+)$',
		DetailView.as_view(
			model=Rule),
		name='docs_rule'),
)
