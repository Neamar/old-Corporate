from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from docs.models import Rule

urlpatterns = patterns('',
	url(r'^$',
		ListView.as_view(
			queryset=Rule.objects.all())),
	url(r'^(?P<slug>[a-z-]+)$',
		DetailView.as_view(
			model=Rule),
		name='docs_rule'),
)
