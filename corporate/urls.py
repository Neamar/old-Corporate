from django.conf.urls import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django import template
template.add_to_builtins('corporate.templatetags.display_entities')

urlpatterns = patterns('',
	url(r'^docs/', include('docs.urls')),
	url(r'^agents/', include('agents.urls')),
	url(r'^corpos/', include('corpos.urls')),
	url(r'^joueurs/', include('joueurs.urls')),
	url(r'^admin/', include(admin.site.urls),),
)
