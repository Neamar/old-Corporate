from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^docs/', include('docs.urls')),
	url(r'^agents/', include('agents.urls')),
	url(r'^corpos/', include('corpos.urls')),
	url(r'^admin/', include(admin.site.urls),),
)
